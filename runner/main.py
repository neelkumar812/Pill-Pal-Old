import command as cmd
from PIL import Image
import pytesseract
import sys
sys.path.append('/Users/i584196/biggestBirds')
from classifier import process_data

def run(text_file, db_string):
    el_fin = process_data.pre_process(text_file, db_string)
    return

def main():

    #configuration
    print("-------------Welcome-------------")
    file_name = input("Enter file name: \n")
    text_file = pytesseract.image_to_string("/Users/i584196/biggestBirds/images/{}".format(file_name))
    db_string = process_data.manipulate_data('/Users/i584196/biggestBirds/images/drug_database.csv')

    #run_test
    run(text_file, db_string)
    

if __name__ == "__main__":
    main()