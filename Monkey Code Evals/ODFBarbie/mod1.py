import odf
from odf.text import P


def convert_odt_to_html(
    input_filename="convertthis.odt", output_filename="output.html"
):
    doc = odf.opendocument.load(input_filename)
    all_paras = doc.getElementsByType(P)

    with open(output_filename, "w") as f:
        f.write("<html><head><style>")
        # Rudimentary CSS - you'll need to customize
        f.write("p { margin-bottom: 10px; }")
        f.write("</style></head><body>")

        for p in all_paras:
            text = p.text
            if text:
                f.write(f"<p>{text}</p>")

        f.write("</body></html>")


# Usage
convert_odt_to_html()
