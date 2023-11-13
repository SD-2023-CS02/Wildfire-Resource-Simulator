from py_pdf_parser.loaders import load_file


FOLDER = "output"


doc = load_file("data/air_tanker_base_directory.pdf")

elements = doc.elements

with open(f"{FOLDER}/elements.txt", "w", errors="ignore") as f:
    for element in elements:
        f.write(element.text() + "\n")
