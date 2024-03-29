import pandas as pd
import numpy as np

def manipulate_data(database):
    df = pd.read_csv(database)
    df['Medicines:'] = df['Medicines:'].str.lower()
    del df[df.columns[0]]
    #print(df)
    db_string = df.values.tolist()
    return db_string
    

def pre_process(txt, db, ac):

    list1 = []
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

    ac1 = ''.join(str(f) for f in ac)
    aac = ''.join(ac1)
    acs1 = aac.replace("["," ")
    acs2 = acs1.replace("]","")
    acs3 = acs2.replace("'","")
    ac_string= acs3.replace(";","")
    #print(ac_string)
    #print(db_string)

    #string matching for medicine name
    for i in prescription:
        temp = list(i.split(' '))
        #print(temp)
        #print(db_string)
        for j in temp:
            item0 = j.replace("[","")
            item1 = item0.replace("]","")
            item1n5 = item1.replace(")","")
            item2 = item1n5.replace("(","")
            item = ' ' + item2 + ' '
            if item in db_string:
                #print('in db_str')
                list1.append(item2)
            #else:
                #print("item not found in db")

    #string matching for action word-sentence
    for i in prescription:
        temp = list(i.split(' '))
        #print(temp)
        #pip3 print(db_string)
        for j in temp:
            item0 = j.replace("[","")
            item1 = item0.replace("]","")
            item1n5 = item1.replace(")","")
            item2 = item1n5.replace("(","")
            item = ' ' + item2 + ' '
            if item in ac_string:
                print('in db_str')
                final= list1+temp
                break
            #else: 
                #print("item not found in ac")

    return final

# def post_process(txt, ac):
#     temp = ' '.join(str(x) for x in txt)
#     for i in ac:
#         before1, _1, after1 = temp.partition(i)
#         print(before1.split()[-1])
#     print(after1)



#     return after1pip[]