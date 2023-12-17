import csv
from os import listdir
from os.path import isfile, join

class Sampler:
    """
    Class used for sampling the correct data from the extraction files.\n
    """
    database_extraction_files_path = 'database_extraction_files'

    def __init__(self, selected_customers, path=""):
        if path != "":
            self.database_extraction_files_path = path
        self.selected_customers = selected_customers
    
    def get_samples(self, list_of_csv_files, path=""):
        """
        Used to extract all the relevant records relating to our sample
        """
        if path == "":
            path = self.database_extraction_files_path

        # Assigning of a local name for convenience
        selected_customers = self.selected_customers
        
        # Ensure alphabetic order so that INVOICE is always executed before INVOICE_ITEM
        sorted(list_of_csv_files)

        customers = []
        invoices = []
        invoice_items = []

        for file in list_of_csv_files:
            with open(path+"\\"+file, 'r') as customers_file:
                reader = csv.reader(customers_file)
                if file == "CUSTOMER.csv":
                    # Create list of dictionaries for the customers csv sample
                    for row in reader:
                        if row[0] in selected_customers:
                            customers.append({"CUSTOMER_CODE": row[0],"FIRSTNAME": row[1],"LASTNAME": row[2]})
                elif file == "INVOICE.csv":
                    # Create list of dictionaries for the invoices csv sample and populate the list of invoice codes
                    invoice_codes = [] # Used as an identifier for the rows we need from the INVOICE_ITEM.csv
                    for row in reader:
                        if row[0] in selected_customers:
                            invoices.append({"CUSTOMER_CODE": row[0],"INVOICE_CODE": row[1], "AMOUNT": row[2], "DATE": row[3]})
                            invoice_codes.append(row[1])
                elif file == "INVOICE_ITEM.csv":
                    # Create list of dictionaries for the invoices csv sample
                    for row in reader:
                        if row[0] in invoice_codes:
                                invoice_items.append({"INVOICE_CODE": row[0], "ITEM_CODE": row[1], "AMOUNT": row[2], "QUANTITY": row[3]})
        return [customers, invoices, invoice_items]

    def get_csv_files_from_directory(self, path=""):
        """
        Used to get all the csv files from the directory specified in the "path" argument.\n
        If a path is not provided, it will default to "database_extraction_files".
        """
        if path != "":
            files_in_directory = listdir(path)
        else:
            files_in_directory = listdir(self.database_extraction_files_path)
        
        files = []
        # Get a list of all the csv files in the directory
        for file in files_in_directory:
            if isfile(join(self.database_extraction_files_path, file)) and file.endswith(".csv"):
                files.append(file)

        # Alternatively we can also use the following list comprehension
        # database_extraction_files = [f for f in listdir(self.database_extraction_files_path) if isfile(join(self.database_extraction_files_path, f) and f.endswith(".csv"))]
        return files