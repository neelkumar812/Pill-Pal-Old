import command as cmd
import pandas as pd
import numpy as np
from PIL import Image
import pytesseract
import sys
sys.path.append('/Users/i584196/biggestBirds')
from classifier import process_data

def run(text_file, db_string, action_string):
    el_fin = process_data.pre_process(text_file, db_string, action_string)
    return el_fin

def main():

    #configuration
    print("-------------Welcome-------------")
    file_name = input("Enter file name: \n")
    text_file = pytesseract.image_to_string("/Users/i584196/biggestBirds/images/{}".format(file_name))
    db_string = process_data.manipulate_data('/Users/i584196/biggestBirds/images/drug_database.csv')

    ac=pd.read_csv('/Users/i584196/biggestBirds/images/action_words.csv')
    del ac[ac.columns[0]]
    ac_string = ac.values.tolist()

    #run_test
    final = run(text_file, db_string, ac_string) #list to be edited by @rochana
    print(final)
    
if __name__ == "__main__":
    main()