import pandas as pd
import numpy as np
import string as str

def manipulate_data(database, text):
    df = pd.read_csv(database)
    df['Medicines:'] = df['Medicines:'].str.lower()
    del df[df.columns[0]]
    #df['Medicines:'] = df['Medicines:'].str.lower()
    print(df)
    db_string = df.values.tolist()
    print(db_string)
    if text in db_string:
        print("in str")
    else:
        print("not in str")
    

def pre_process(txt):
    #print("{}".format(txt_file))
    print(txt)
    concat = ''.join(txt.splitlines())
    concat = concat.lower()
    print(concat)
    return concat