#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print (enron_data[enron_data.keys()[0]])  

poi=0
stock=0
mailstopoi=0
exercised_stock_options=0
total_payments=0
name_max=0
for i in enron_data :
    if(enron_data[i]["poi"]==1) :
        poi=poi+1
        
for i in enron_data :
    if "PRENTICE JAMES" in i :
            stock=stock+enron_data[i]["total_stock_value"]

    if "COLWELL WESLEY" in i :
            mailstopoi=mailstopoi+enron_data[i]["from_this_person_to_poi"]

    if "SKILLING JEFFREY" in i :
            exercised_stock_options=exercised_stock_options+enron_data[i]["exercised_stock_options"]

    if "LAY" in i :
            if total_payments<enron_data[i]["total_payments"] :
                total_payments=enron_data[i]["total_payments"]
                name_max=i
    elif "SKILLING" in i :
            if total_payments<enron_data[i]["total_payments"] :
                total_payments=enron_data[i]["total_payments"]
                name_max=i
    elif "FASTOW" in i :
            if total_payments<enron_data[i]["total_payments"] :
                total_payments=enron_data[i]["total_payments"]
                name_max=i
            
            
salaried=0 
emailed=0 
NanTotalPayment=0  
for i in enron_data :
    if(enron_data[i]["salary"]!='NaN') :
        salaried=salaried+1
    if(enron_data[i]["email_address"]!="NaN") :
        emailed=emailed+1
    if enron_data[i]["total_payments"]=="NaN" :
        NanTotalPayment=NanTotalPayment+1
        print i
   
print stock
print poi 
print mailstopoi 
print exercised_stock_options
print total_payments  
print name_max    
print salaried
print emailed
print NanTotalPayment
print len(enron_data)
