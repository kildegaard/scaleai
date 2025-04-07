from flask import (
    Flask,
    request,
    send_file,
    session,
    redirect,
    url_for,
    render_template_string,
)
from PIL import Image
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Replace with your secret key
app.config["UPLOAD_FOLDER"] = "images"


@app.route("/")
def index():
    return render_template_string(open("gallery.html").read())


@app.route("/select-image", methods=["POST"])
def select_image():
    session["selected_image"] = request.form["image"]
    return "Image selected: " + session["selected_image"]


@app.route("/export")
def export_image():
    if "selected_image" not in session:
        return redirect(url_for("index"))

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], session["selected_image"])
    format = request.args.get("format", "jpg")

    with Image.open(image_path) as img:
        converted_image_path = os.path.join(
            app.config["UPLOAD_FOLDER"], f"converted_image.{format}"
        )
        img.save(converted_image_path, format=format.upper())

    return send_file(
        converted_image_path, as_attachment=True, download_name=f"image.{format}"
    )


if __name__ == "__main__":
    app.run(debug=True)
