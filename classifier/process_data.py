import pandas as pd
import numpy as np


def manipulate_data(database):
    df = pd.read_csv(database)
    df['Medicines:'] = df['Medicines:'].str.lower()
    del df[df.columns[0]]
    #print(df)
    db_string = df.values.tolist()
    return db_string
    

def pre_process(txt, db):

    #creating list from the string
    txt=txt.lower()
    lxst = list(txt.split('\n'))
    prescription = [x for x in lxst if x != '']
    #print(prescription)


    #more manipulation
    db_string_not_yet = ''.join(str(e) for e in db)
    #print(db_string_not_yet)
    db_strrrr = ''.join(db_string_not_yet)
    db1 = db_strrrr.replace("["," ")
    db2 = db1.replace("]","")
    db3 = db2.replace("'","")
    db_string= db3.replace(";","")
    
    print(db_string)

    #string matching for medecine name
    for i in prescription:
        temp = list(i.split(' '))
        print(temp)
        #print(db_string)
        for j in temp:
            item = ' ' + j + ' '
            if item in db_string:
                print('in db_str')
            else: 
                print('not in db_str')

    # temp = list(presc.split(' '))
    # for i in range(len(presc)):
        
    #     for j in range(len(temp)):
    #         if temp()
            

        











    return txt