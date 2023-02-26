import command as cmd
import pandas as pd
import numpy as np
from PIL import Image
import pytesseract
import sys
sys.path.append('/Users/i584196/biggestBirds')
import json

from classifier import process_data

def run(text_file, db_string, action_string):
    el_fin = process_data.pre_process(text_file, db_string, action_string)
    return el_fin

def main():

    #configuration
    print("-------------Welcome-------------")
    file_name = input("Enter file name: \n")
    text_file = pytesseract.image_to_string("/Users/i584196/biggestBirds/images/{}".format(file_name))
    print(text_file)
    db_string = process_data.manipulate_data('/Users/i584196/biggestBirds/images/drug_database.csv')

    ac=pd.read_csv('/Users/i584196/biggestBirds/images/action_words.csv')
    del ac[ac.columns[0]]
    ac_string = ac.values.tolist()
  
    #run_test
    final = run(text_file, db_string, ac_string) #list to be edited by @rochana

    #post_process data
    #output = process_data.post_process(final,ac_string)
    list_final = []
    temp_final = ' '.join(str(x) for x in final)
    keyword1 = 'take'
    before1, _1, after1 = temp_final.partition(keyword1)
    #print(before1.split()[-1])
    list_final.append(before1.split()[-1])
    keyword = 'tab'
    before, _, after = temp_final.partition(keyword)
    #print(before.split()[-1])
    #print(after.split()[0])

    list_final.append(before.split()[-1])
    list_final.append(after.split()[0])
    #print(list_final)

    #convert output to json
    jsonStr = json.dumps(list_final)
    with open('presc.json', 'w') as f:
        f.write(jsonStr)

if __name__ == "__main__":
    main()