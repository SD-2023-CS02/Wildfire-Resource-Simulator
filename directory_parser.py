from py_pdf_parser.loaders import load_file

# Retrieve Base Name index 0
# Latitude longitude index 2
# Geographic area? index 3 after "Base Location"
# Runway weight limits: single, dual, 2S, 2D 
#   if there's not a phone number before "Runway weight limits"... collect all numbers between each subtitle (single, double, etc)
# VLATs, Pit Total, Hot Loading, LATs, Parking Total, Fuel and Load, MAFFS, Load Simultaneously, 
#   Hot Refueling, SEATs, Offload Capacity, Reserved
#   parse values between titles ... if dne the other titles, make sure there are enough to sort,
# Retardant Jettison Area(s)
#   if it contains 'Lat' and 'Long' or numbers and 'N' and 'W'

class DirectoryParser:
    def __init__(self, file_path, folder="output"):
        self.file_path = file_path
        self.folder = folder
        self.pages = []
        self.load_data()


    def load_data(self):
        doc = load_file(self.file_path)
        elements = doc.elements

        with open(f"{self.folder}/elements.txt", "w", errors="ignore") as f:
            for element in elements:
                f.write(element.text() + "\n")

    #def get_runway_weight_lims(self):
        # Runway weight limits: single, dual, 2S, 2D 
        #   if there's not a phone number before "Runway weight limits"... collect all numbers between each subtitle (single, double, etc)

    #def get_load_limits(self):
        # VLATs, Pit Total, Hot Loading, LATs, Parking Total, Fuel and Load, MAFFS, Load Simultaneously, 
        #   Hot Refueling, SEATs, Offload Capacity, Reserved
        #   parse values between titles ... if dne the other titles, make sure there are enough to sort,

    #def get_jettison_area(self):
        # Retardant Jettison Area(s)
        #   if it contains 'Lat' and 'Long' or numbers and 'N' and 'W'

    def process_page(self, page_data):
        base_info = {}
        base_info['Base Name'] = page_data[0].split('�')[0]
        base_info['Airport'] = page_data[1]
        base_info['Latitude,Longitude'] = page_data[2]
        base_info['Geographic Area'] = page_data[4]

        return base_info


    def parse_directory(self):
        with open(f'{self.folder}/elements.txt', 'r') as file:
            data = file.readlines()

        pages = []
        current_page = []

        for line in data:
            if 'of 144' in line:
                pages.append(current_page)  # excludes 'of 144' line
                current_page = []
            else:
                current_page.append(line.strip())
        
        for idx, page in enumerate(pages, start=1):
            base_info = self.process_page(page)
            print(f"Base {idx} Information:")
            
            for key, value in base_info.items():
                print(f"{key}: {value}")
            print()
