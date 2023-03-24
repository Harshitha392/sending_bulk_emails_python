# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:49:47 2022

@author: harsh
"""

from email.message import EmailMessage
import smtplib 
import csv

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com',587) #set up a connection with smtp server
    #587 is port number
    smtpObj.ehlo()   #ehlo checks if the connection is working or not
    #ehlo will give error if connection is not ok
    smtpObj.starttls() # transport layer security
    #the above line checks if the connection is secure or not
    id='demo_account@gmail.com'  #demo email
    pwd='demo123!'       #demo password
    smtpObj.login(id,pwd) #to login the email
    msg = EmailMessage()  #create email message object
    #msg[to],msg[subject],msg[content]
   # msg["From"] ="Harshitha"
    #msg["To"] = "temporaryemailid.gmail.com" #this is temporary email and will get expired also
    #msg["Subject"] = "Testing"
    #msg.set_content("How are you?") #gmail is secure so we have to allow access on low security apps in setting of google account
   
    #SENDING BULK EMAILS
    #create a file in google spreadsheet containing the below columns and download it as csv file and put it in same folder as this project file
    #csv file containing columns : from ,to ,subject ,content
    
    
    with open('all_email.csv', 'r ') as email_file:
        csv_reader = csv.DictReader(email_file)  #converting each thing to dictionary
        #check the columns of this dict
        #for row in csv_reader:
          #  print(row)
        
        for row in csv_reader:
            msg["To"] = row["To"]
            msg["From"] = row["From"]
            msg["Subject"] = row["Subject"]
            msg.set_content(row["Content"])
        
    smtpObj.send_message(msg) #sends email to given email id
    
    smtpObj.quit() #will quite current smtp connection
    
    
    
    
except Exception as err:
    print(err)