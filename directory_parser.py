from py_pdf_parser.loaders import load_file

class DirectoryParser:
    def __init__(self, file_path, folder="output"):
        self.file_path = file_path
        self.folder = folder
        self.pages = []
        self.load_data()

    def load_data(self):
        doc = load_file("data/air_tanker_base_directory.pdf")
        elements = doc.elements

        with open(f"{self.folder}/elements.txt", "w", errors="ignore") as f:
            for element in elements:
                f.write(element.text() + "\n")

    def process_page(self, page_data):
        base_info = {}
        base_info['Base Name'] = page_data[0].split('�')[0]
        base_info['Airport'] = page_data[1]
        base_info['Latitude,Longitude'] = page_data[2]
        base_info['Base Location on Field'] = page_data[3]
        return base_info

    def parse_directory(self):
        with open(f'{self.folder}/elements.txt', 'r') as file:
            data = file.readlines()

        pages = []
        current_page = []
        for line in data:
            current_page.append(line)
            if 'of 144' in line:
                pages.append(current_page[:-1])  # Remove the 'of 144' line
                current_page = []

        for idx, page in enumerate(pages, start=1):
            base_info = self.process_page(page)
            print(f"Base {idx} Information:")
            for key, value in base_info.items():
                print(f"{key}: {value}")
            print("\n")