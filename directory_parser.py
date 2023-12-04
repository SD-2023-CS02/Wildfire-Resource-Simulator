from py_pdf_parser.loaders import load_file

class DirectoryParser:
    """
    A class to parse information from a pdf file containing data related to air tanker bases.
    The original pdf can be found at this link: 
    https://ftp.wildfire.gov/public/incident_specific_data/n_rockies/IncidentAviationManagers/AirTanker-Retardant/pms507-ATB-directory2018.pdf

    Attributes:
        pages (list): A list containing parsed pages from the directory file.

    Methods:
        load_data(file_path, folder="output"): Loads data from the specified file_path and writes it to a text file.
        get_runway_weight_lims(page): Retrieves runway weight limits information from the given page.
        find_next_line(lines, start_index, expected_values): Finds the next line based on specified conditions.
        get_load_limits(table_label, page): Retrieves load limits information based on specific table labels.
        process_page(page_data): Processes each page and extracts relevant information such as base name, airport, etc.
        parse_directory(folder, fname): Parses the entire directory file and prints extracted information for each base.
    """


    def __init__(self):
        """
        Constructor method initializing the DirectoryParser class. Initializes the 'pages' attribute as an empty list to 
        store parsed pages.
        """
        self.pages = []


    def load_data(self, file_path, folder="output"):
        """
        Loads data from the specified file_path and writes it to a text file in the given folder.

        Args:
            file_path (str): The path to the directory file.
            folder (str): The folder to store the parsed data. Defaults to "output".
        """
        doc = load_file(file_path)
        elements = doc.elements

        with open(f"{folder}/elements.txt", "w", errors="ignore") as f:
            for element in elements:
                f.write(element.text() + "\n")


    def get_runway_weight_lims(self, page):
        """
        Retrieves runway weight limits information from the given page.

        Args:
            page (list): The page containing information to retrieve runway weight limits.
        Returns:
            dict: A dictionary containing runway weight limit information.
       
        NOTE: only retrieves first listed value for each limit... following values are read by the parser in an 
        unpredicatable way)
        """
        limits = {}
        runway_limits_started = False

        back_tracker = 0 # sometimes values are loaded before the 'Runway Weight Limits' label, so check up to 15 lines before label
        for i in range(0, len(page)):
            if 'Runway Weight Limits' in page[i]:
                runway_limits_started = True
                back_tracker = i - 15
            elif runway_limits_started: # once we've identified the section of the txt file where the information is stored
                line = page[back_tracker]
                if line == 'Single' or line == 'Dual' or line == '2S' or line == '2D':
                    runway_type = line.split()[0]
                    next_line = page[back_tracker+1]
                    if next_line[:2].isdigit():
                        limits[runway_type] = next_line.strip()
                if line == 'VLAT': # if we reach this line, we know we'ved moved past the 'Runway Weight Limits' section
                    break
                back_tracker += 1

        return limits


    def find_next_line(self, lines, start_index, expected_values):
        """
        Finds the next line based on specified conditions starting from the provided index.

        Args:
            lines (list): A list of lines to search within.
            start_index (int): The starting index for the search.
            expected_values (list): List of expected values to find.
        Returns:
            tuple: Index and line found based on the specified conditions.
        
        NOTE: improvement: some YES or NO lines aren't capitalized or have a footnote so appear as 'YES1' for example
        """
        for i in range(start_index, len(lines)):
            line = lines[i].strip()
            if line not in expected_values and not line.isdigit():
                continue
            return i, line


    def get_load_limits(self, table_label, page):
        """
        Retrieves load limits information based on specific table labels from the given page.

        Args:
            table_label (list): List containing labels for load limits.
            page (list): The page containing information to retrieve load limits.
        Returns:
            dict: A dictionary containing load limits information.
        """
        load_limits = {}
        expected_yes_no = ['YES', 'NO']

        for i, line in enumerate(page):
            if table_label[2] in line: # if we reach the last of the three labels in the group, the values should start to show up
                start_section = self.find_next_line(page, i + 1, expected_yes_no)
                if start_section is None: # make sure there's a line to check
                    continue
                
                start_section_index, start_line = start_section
                if start_line not in expected_yes_no:
                    continue
                load_limits[table_label[0]] = start_line # if the first value is 'YES' or 'NO', we can assume it matches the label and store it as such

                second_section = self.find_next_line(page, start_section_index + 1, expected_yes_no)
                if second_section is None:
                    continue

                second_index, second_line = second_section
                if second_line.isdigit(): # if the second value is a digit, we can assume it matches the second label and store it as such
                    load_limits[table_label[1]] = second_line

                third_section = self.find_next_line(page, second_index + 1, expected_yes_no)
                if third_section is None:
                    continue

                third_index, third_line = third_section
                if third_line in expected_yes_no: # the third value should also be either 'YES' or 'NO'
                    load_limits[table_label[2]] = third_line
                
                break
        return load_limits

    def process_page(self, page_data):
        """
        Processes a page and extracts relevant information such as base name, airport, etc.

        Args:
            page_data (list): The page data to process.
        Returns:
            dict: A dictionary containing extracted information from the page.
        """
        base_info = {}
        base_info['Base Name'] = page_data[0].split('�')[0]
        base_info['Airport'] = page_data[1]
        base_info['Latitude, Longitude'] = page_data[2]
        base_info['Geographic Area'] = page_data[4]

        base_info['Runway Weight Limits'] = self.get_runway_weight_lims(page_data)
        vlat_limits = self.get_load_limits(['VLATs', 'Pit Total', 'Hot Loading'], page_data)
        base_info['VLATs'] = vlat_limits
        lat_limits = self.get_load_limits(['LATs', 'Parking Total', 'Fuel and Load'], page_data)
        base_info['LATs'] = lat_limits
        maffs_limits = self.get_load_limits(['MAFFS', 'Load Simultaneously', 'Hot Reloading'], page_data)
        base_info['MAFFS'] = maffs_limits

        return base_info


    def parse_directory(self, folder, fname):
        """
        Parses the entire directory file and prints extracted information for each base.

        Args:
            folder (str): The folder where the file is located.
            fname (str): The name of the file to parse.
        """
        with open(f'{folder}/{fname}', 'r') as file:
            data = file.readlines()

        current_page = []

        for line in data: # break the txt file into pages based on our knowledge that the last line will have pg# 'of 144'
            current_page.append(line.strip())
            if 'of 144' in line:
                self.pages.append(current_page)
                current_page = []
        
        for idx, page in enumerate(self.pages, start=1): # print the collected information
            base_info = self.process_page(page)
            print(f"Base {idx} Information:")
            
            for key, value in base_info.items():
                print(f"{key}: {value}")
            print()
