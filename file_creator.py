# IMPORT MODULES
import shutil  # Provides higher level interface for file operations
from datetime import date  # Provides functions for working with dates and times
import time
import os  # Provides a way to interact with the operating system

SAQ_Type = ['A', 'C-VT']

#Set up Variables
Company_Name = str(input("Enter Company Name: "))  # Prompts user for company name
iso = date.today().isoformat()  # Gets today's date in ISO format
iso = iso.replace("-","")  # Strips hyphens from the date string
MetaData = Company_Name + iso  # Concatenates company name and date to form metadata string
File_Destination = "Documents/"


for i in range(len(SAQ_Type)-1):
  SAQType = SAQ_Type[i]
  if SAQType == "A" :  # If SAQ type is "A"
    File_Name = MetaData + "_SAQ_A"
    File_Data = File_Destination + File_Name 
    shutil.copyfile("Templates/SAQA.txt", File_Data)  
  elif SAQType == "A-EP" :
    File_Name = MetaData + "_SAQ_E-IP" 
    File_Data = File_Destination + File_Name 
    shutil.copyfile("Templates/SAQEIP.txt", File_Data) 
  
  elif SAQType == "P2PE" :
    File_Name = MetaData + "_SAQ_P2PE"  
    File_Data = File_Destination + File_Name 
    shutil.copyfile("Templates/SAQP2PE.txt", File_Data)  
	
  elif SAQType == "B" :
  		File_Name = MetaData + "_SAQ_B"  
	  	File_Data = File_Destination + File_Name  
	  	shutil.copyfile("Templates/SAQB.docx", File_Data) 

  elif SAQType == "B-IP":
  		File_Name = MetaData + "_SAQ_B-IP"
  		File_Data = File_Destination + File_Name  
	  	shutil.copyfile("Templates/SAQB-IP.docx", File_Data)

  elif SAQType == "C" :
  		File_Name = MetaData + "_SAQ_C" 
  		File_Data = File_Destination + File_Name 
  		shutil.copyfile("Templates/SAQC.docx", File_Data) 

  elif SAQType == "C-VT" :
    File_Name = MetaData + "_SAQ_C-VT"
    File_Data = File_Destination + File_Name 
    shutil.copyfile("Templates/SAQC.docx", File_Data) 

  elif SAQType == "D" :
  		PROV_MER = input("For Providers or Merchant: ")
  		if PROV_MER.lower() == "Providers" :
    
    			File_Name = MetaData + "_SAQ_D_Providers" 
    			File_Data = File_Destination + File_Name 
    			shutil.copyfile("Templates/SAQDProvider.docx", File_Data) 
      
  else:
    			File_Name = MetaData + "_SAQ_D_Merchant" 
    			File_Data = File_Destination + File_Name 
    			shutil.copyfile("Templates/SAQDMerchant.docx", File_Data) 


print("Reports Generated")
time.sleep(10)
os.system("clear")  # Clears the terminal screen again
