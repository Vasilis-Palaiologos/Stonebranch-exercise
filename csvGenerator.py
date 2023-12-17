import names
import csv
from random import choice, randrange

class csvGenerator:
    """
    This is a helper class I created.\n
    It's used for the creation of csv files
    """

    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    item_codes = ["MEIJI", "POCKY", "PUCCHO"]

    def __init__(self, number_of_customers=50):
        number_of_invoices = number_of_customers * 2
        number_of_invoice_items = number_of_invoices * 5

        # Make a list of dictionaries of randomly generated customers
        self.customers = []
        for i in range(0, number_of_customers):
            customer_code = "CUST_" + str(i)
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            self.customers.append({"CUSTOMER_CODE": customer_code,"FIRSTNAME": first_name,"LASTNAME": last_name})
        
        # Make a list of dictionaries of randomly generated invoices that relate to the customers above
        self.invoices = []
        for i in range(0, number_of_invoices):
            customer_code = choice(self.customers)['CUSTOMER_CODE']
            invoice_code = "IN_" + str(i)
            amount = str(randrange(1,10))
            date = "-".join((str(randrange(1,31)), choice(self.months),"2016"))
            self.invoices.append({"CUSTOMER_CODE": customer_code, "INVOICE_CODE": invoice_code, "AMOUNT": amount, "DATE": date})
        
        # Make a list of dictionaries of randomly generated invoice items that relate to the invoices above
        self.invoice_items = []
        for i in range(0, number_of_invoice_items):
            invoice = choice(self.invoices)

            invoice_code = invoice["INVOICE_CODE"]
            item_code = choice(self.item_codes)
            amount = str(randrange(1,10))
            quantity = str(randrange(0, 200))
            self.invoice_items.append({"INVOICE_CODE": invoice_code, "ITEM_CODE": item_code, "AMOUNT": amount, "QUANTITY": quantity})

    # Create all of the csv files at once (only used to improve code readbility)
    def create_all_csv_files(self, list_of_lists_of_dictionaries=[]):
        """
        Used to create all of the required csv files at once, to improve code readability\n
        """
        if list_of_lists_of_dictionaries:
            self.create_customer_csv_file("CUSTOMER", list_of_lists_of_dictionaries[0])
            self.create_invoice_csv_file("INVOICE", list_of_lists_of_dictionaries[1])
            self.create_invoice_item_csv_file("INVOICE_ITEM", list_of_lists_of_dictionaries[2])
        else:
            self.create_customer_csv_file("CUSTOMER", self.customers)
            self.create_invoice_csv_file("INVOICE", self.invoices)
            self.create_invoice_item_csv_file("INVOICE_ITEM", self.invoice_items)

    # Create the CUSTOMER.csv file
    def create_customer_csv_file(self, file_name, list_of_dictionaries):
        """
        Used to create a csv file with the template of CUSTOMER.csv\n
        """
        header = ["CUSTOMER_CODE", "FIRSTNAME", "LASTNAME"]

        with open('database_extraction_files\\'+file_name+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(list_of_dictionaries)

    # Create the INVOICE.csv file
    def create_invoice_csv_file(self, file_name, list_of_dictionaries):
        """
        Used to create a csv file with the template of INVOICE.csv\n
        """
        header = ["CUSTOMER_CODE", "INVOICE_CODE", "AMOUNT", "DATE"]

        with open('database_extraction_files\\'+file_name+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(list_of_dictionaries)

    # Create the INVOICE_ITEM.csv file
    def create_invoice_item_csv_file(self, file_name, list_of_dictionaries):
        """
        Used to create a csv file with the template of INVOICE_ITEM.csv\n
        """
        header = ["INVOICE_CODE", "ITEM_CODE", "AMOUNT", "QUANTITY"]

        with open('database_extraction_files\\'+file_name+'.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(list_of_dictionaries)