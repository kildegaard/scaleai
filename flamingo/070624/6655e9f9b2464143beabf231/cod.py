import urllib.request
import re
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Tuple, Callable
from io import BytesIO
from math import ceil, inf, sqrt
from random import choices
from PIL import Image, ImageDraw, ImageFont

# Assume the following two imports have been implemented correctly:
from musicapp.albums import get_top_albums
from musicapp.resources import FONT_TTF

# Assume the above two imports have been implemented correctly.


SUBTITLE_REGEX = r"(\d+)?(\w+)"
SUBTITLE_PATTERN = re.compile(SUBTITLE_REGEX)


def __get_image(url: str, *, size_constraint: Tuple[int, int] = None) -> Image:
    """Get a PIL image from a URL.

    :param url: URL to get Image from.
    :type url: str
    :param size_constraint: Resize image to size, defaults to None
    :type size_constraint: Tuple[int, int], optional
    :raises RuntimeError: http request to download image fails.
    :raises TypeError: size_constraint is not None or tuple[int, int]
    :raises ValueError: size_constraint is of invalid dimensions.
    :return: Downloaded image.
    :rtype: Image
    """
    data = BytesIO()
    with urllib.request.urlopen(url) as request:
        if request.status != 200:
            raise RuntimeError("http request failed with status code", request.status)
        else:
            chunk = request.read()
            while chunk:
                data.write(chunk)
                chunk = request.read()
    image = Image.open(data)
    # Resize if necessary
    if not size_constraint is None:
        if not isinstance(size_constraint, tuple):
            raise TypeError("size_constraint should be of type tuple[int, int]")
        if len(size_constraint) != 2:
            raise ValueError(
                "Invalid size_constraint dimensions. Should be 2 ([int, int])."
            )
        if not isinstance(size_constraint[0], int) or not isinstance(
            size_constraint[1], int
        ):
            raise TypeError("size_constraint should be of type tuple[int, int]")
        image = image.resize(size_constraint)

    return image


def __k_means(
    population: list,
    cluster_count: int,
    distance_formula: Callable[[any, any], float],
    *,
    MAX_ITERATIONS: int = 30,
    initial_weights=None,
) -> dict:
    """Perform k-means on a population to find clusters.

    :param population: Population of elements.
    :type population: list
    :param cluster_count: How many clusters to create.
    :type cluster_count: int
    :param distance_formula: Distance formula for finding nearest elements.
    :type distance_formula: Callable[[any, any], float]
    :param MAX_ITERATIONS: max iterations, defaults to 30
    :type MAX_ITERATIONS: int, optional
    :return: Clusters. Keys are centroids.
    :rtype: dict
    """
    # Initial centroids
    centroids = choices(population, k=cluster_count, weights=initial_weights)
    iterations = 0
    convergence = False
    while (not convergence) and (iterations < MAX_ITERATIONS):
        iterations += 1
        # Build clusters
        clusters = {centroid: [] for centroid in centroids}
        # Assign clusters for each element
        for element in population:
            min_distance = inf
            min_centroid = None
            for centroid in centroids:
                distance = distance_formula(element, centroid)
                if distance < min_distance:
                    min_distance = distance
                    min_centroid = centroid
            clusters[min_centroid].append(element)
        # Find new centroids
        new_centroids = []
        for elements in clusters.values():
            if len(elements) == 0:
                continue
            summed_element = [
                sum([element[i] for element in elements])
                for i in range(len(elements[0]))
            ]
            centroid = tuple(band // cluster_count for band in summed_element)
            new_centroids.append(centroid)
        # Check for convergence
        convergence = True
        for old, new in zip(centroids, new_centroids):
            for old_band, new_band in zip(old, new):
                if old_band != new_band:
                    convergence = False
                    break
            if not convergence:
                break
    return clusters


def __color_distance(
    color_a: tuple[int, int, int], color_b: tuple[int, int, int]
) -> float:
    """Return the difference between two colors.

    :param color_a: First color
    :type color_a: tuple[int, int, int]
    :param color_b: Second color
    :type color_b: tuple[int, int, int]
    :return: Color distance
    :rtype: float
    """
    # Euclidian distance formula
    return sum([(band[0] - band[1]) ** 2 for band in zip(color_a, color_b)]) ** 0.5


def __get_dominant_color(image: Image) -> Tuple[int, int, int]:
    """Get the dominant color from the image.

    :param image: Image to use
    :type image: Image
    :return: Dominant color
    :rtype: Tuple[int, int, int]
    """

    # Flatten pixel list
    pixels: list[tuple[int, int, int]] = []
    width, height = image.size
    for y in range(height):
        for x in range(width):
            coordinate = (x, y)
            pixels.append(image.getpixel(coordinate))

    # Find palette
    palette_count = 6
    palettes = __k_means(pixels, palette_count, __color_distance)
    # Find the most prominant palette
    max_palette_size = -inf
    dominant_color = None
    for palette, pixels in palettes.items():
        palette_size = len(pixels)
        if palette_size > max_palette_size:
            max_palette_size = palette_size
            dominant_color = palette
    return (dominant_color, max_palette_size)


def get_chart(username: str, period: str, rows: int, cols: int) -> Image:
    """Get a chart for a user.

    :param username: Username of user to get chart from.
    :type username: str
    :param period: Period of time to get chart from.
    :type period: str
    :param rows: Rows of chart.
    :type rows: int
    :param cols: Columns of chart.
    :type cols: int
    :raises ValueError: Rows or columns are <= 0.
    :return: Generated chart image.
    :rtype: Image
    """

    if rows <= 0:
        raise ValueError("Rows must be > 0")
    if cols <= 0:
        raise ValueError("Cols but be > 0")

    albums = get_top_albums(username, period, rows * cols)

    # Rendering

    # Constants
    PADDING_X: int = 10
    PADDING_Y: int = 10

    ALBUM_SIZE: int = 128
    FONT_SIZE: int = 20

    # Get dominant album color for background color
    album_images = {
        album["image"]: __get_image(
            album["image"], size_constraint=(ALBUM_SIZE, ALBUM_SIZE)
        )
        for album in albums
    }
    dominant_colors = [__get_dominant_color(image) for image in album_images.values()]
    # Find the most dominant of the most dominant colors
    colors = [color[0] for color in dominant_colors]
    weights = [color[1] for color in dominant_colors]
    grouped_dominants = __k_means(
        colors, 3, __color_distance, MAX_ITERATIONS=10, initial_weights=weights
    )
    most_dominant_color = None
    max_dominance_ranking = -inf
    for cluster, elements in grouped_dominants.items():
        ranking = len(elements)
        if ranking > max_dominance_ranking:
            most_dominant_color = cluster
            max_dominance_ranking = ranking
    background_color = most_dominant_color
    background_luminance = (
        sqrt(
            0.299 * background_color[0] ** 2
            + 0.587 * background_color[1] ** 2
            + 0.114 * background_color[2] ** 2
        )
        / 255
    )

    # Load font
    font = ImageFont.truetype(font=bytes(FONT_TTF), size=FONT_SIZE)
    larger_font = ImageFont.truetype(font=bytes(FONT_TTF), size=FONT_SIZE * 2)
    font_color = (255, 255, 255)
    if background_luminance > 0.5:
        font_color = (0, 0, 0)

    # Album text formatter
    form_album_text = lambda album: f"{album['artist']} - {album['title']}"

    # Get max text width/height
    bboxes = [font.getbbox(form_album_text(album)) for album in albums]
    bbox_height = lambda bbox: bbox[3] - bbox[1]
    bbox_width = lambda bbox: bbox[2] - bbox[0]
    max_text_width = max([bbox_width(bbox) for bbox in bboxes])
    max_text_height = max([bbox_height(bbox) for bbox in bboxes])

    # Calculate whether the height of the albums or text will be taller to prevent text/image cutoff
    max_height_by_album = (rows * ALBUM_SIZE) + ((rows + 1) * PADDING_Y)
    max_height_by_text = ((rows + 1) * PADDING_Y) + (max_text_height * len(albums))

    # Titlebar
    # Title formatting
    timezone = ZoneInfo("EST")
    title = datetime.now(tz=timezone).strftime("%B %d, %Y")
    title_bbox = larger_font.getbbox(title)

    # Subtitle formatting
    matches = SUBTITLE_PATTERN.fullmatch(period)
    subtitle = " ".join((matches[1], matches[2])).title() + " Chart"
    subtitle_bbox = font.getbbox(subtitle)

    # Height calculation
    titlebar_offset = (
        (PADDING_Y * 3) + bbox_height(title_bbox) + bbox_height(subtitle_bbox)
    )

    # Get image width + height
    image_width = (
        ceil((cols * ALBUM_SIZE) + ((cols + 2) * PADDING_X) + (max_text_width))
        + PADDING_X
    )
    image_height = max(max_height_by_album, max_height_by_text) + titlebar_offset

    # Create image objects
    chart = Image.new("RGB", (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(chart)

    # Render image
    # Draw titlebar
    subtitle_y = (PADDING_Y * 2) + bbox_height(title_bbox)
    draw.text((PADDING_X, PADDING_Y), title, font=larger_font, fill=font_color)
    draw.text((PADDING_X, subtitle_y), subtitle, font=font, fill=font_color)

    text_x = (cols + 2) * PADDING_X + (cols * ALBUM_SIZE)

    for album in albums:
        rank = album["rank"]
        col = rank % cols
        row = rank // cols

        # Draw image
        album_x = (col + 1) * PADDING_X + (col * ALBUM_SIZE)
        album_y = (row + 1) * PADDING_Y + (row * ALBUM_SIZE) + titlebar_offset

        album_image = album_images[album["image"]]
        chart.paste(album_image, (album_x, album_y))

        # Draw text
        text = form_album_text(album)
        text_y = ((row + 1) * PADDING_Y) + (max_text_height * rank) + titlebar_offset
        draw.text((text_x, text_y), text, font=font, fill=font_color)

    return chart
