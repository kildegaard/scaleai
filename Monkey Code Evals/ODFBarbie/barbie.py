import odf.opendocument
from odf.text import H, P
from odf.style import Style, TextProperties, ParagraphProperties


def convert_odt_to_html(odt_filename="convertthis.odt"):
    """Converts an ODT file to HTML with CSS styling."""

    # Load the ODT file
    doc = odf.opendocument.load(odt_filename)

    # Extract styles (this is essential for formatting)
    styles = doc.styles

    # Create CSS dictionary
    css_styles = {}
    for style in styles.getElementsByType(Style):
        css_styles[style.getAttribute("name")] = create_css_style(style)

    # Prepare HTML output
    html = ["<html><head><style>"]
    html.append("\n".join(css_styles.values()))
    html.append("</style></head><body>")

    # Process the content element (main body of the ODT)
    content = doc.text
    for element in content.childNodes:
        html.append(process_element(element, css_styles))

    html.append("</body></html>")

    # Save HTML
    html_filename = odt_filename.replace(".odt", ".html")
    with open(html_filename, "w") as f:
        f.writelines("\n".join(html))

    print(f"ODT file converted to HTML: {html_filename}")


def process_element(element, css_styles):
    """Recursively processes ODT elements and converts them to HTML."""
    if element.tagName == "text:h":
        level = get_attribute(element, "outline-level", default=1)
        return f"<h{level}>{element.firstChild.data}</h{level}>"
    elif element.tagName == "text:p":
        style_name = get_attribute(element, "style-name")
        if style_name:
            return f'<p class="{style_name}">{element.firstChild.data}</p>'
        else:
            return f"<p>{element.firstChild.data}</p>"
    else:
        # Handle other potential element types if needed
        return str(element)


def get_attribute(element, attribute_name, default=None):
    """Retrieves the attribute by local name."""
    for attr in element.attributes.items():
        if attr[0].localName == attribute_name:
            return attr[1]
    return default


def create_css_style(style):
    """Creates a CSS style string from an ODF style object."""
    css = []
    if style.getAttribute("name"):
        css.append("." + style.getAttribute("name") + " {")
        for prop in style.childNodes:
            if prop.tagName == "style:text-properties":
                for key, value in prop.attributes.items():
                    css.append(f"  {key[1].replace('fo:', '')}: {value};")
            elif prop.tagName == "style:paragraph-properties":
                for key, value in prop.attributes.items():
                    css.append(f"  {key[1].replace('fo:', '')}: {value};")
        css.append("}")
    return "\n".join(css)


# Execute the conversion
convert_odt_to_html()
