import command as cmd
from PIL import Image
import pytesseract
import sys
sys.path.append('/Users/i584196/biggestBirds')
from classifier import process_data



txt_file= pytesseract.image_to_string("/Users/i584196/biggestBirds/images/test_chlor.jpeg")
concat = process_data.pre_process(txt_file)

process_data.manipulate_data('drug_database.csv', concat)





