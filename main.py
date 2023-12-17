import csv
import sys
from Sampler import Sampler
from csvGenerator import csvGenerator

if __name__ == "__main__":
    csv_gen = csvGenerator()
    # csv_gen.create_all_csv_files()
    customer_code_list = []
    if len(sys.argv) >= 2:
        if sys.argv[1]:
            sample_file_path = sys.argv[1]
    else:
        print("Please provide a path to the sample file")
        sys.exit(-1)
    try:
        with open(sample_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                customer_code_list.append(row[0])
    except Exception as e:
        print("Please provide a valid file-path to the sample file")
        sys.exit()
    
    sampler = Sampler(customer_code_list)
    list_of_csv_files = sampler.get_csv_files_from_directory()
    samples_list = sampler.get_samples(list_of_csv_files)
    
    csv_gen.create_customer_csv_file("CUSTOMER_SAMPLE", samples_list[0])
    csv_gen.create_invoice_csv_file("INVOICE_SAMPLE", samples_list[1])
    csv_gen.create_invoice_item_csv_file("INVOICE_ITEM_SAMPLE", samples_list[2])