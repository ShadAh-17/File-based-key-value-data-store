import threading
from threading import*
import time

#'d' is the dictionary in which we store data
d={} 

# Create Operation

def create(key,value,timeout=0):
    if key in d:
        print("Error: Key already exists") # Error message 1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): # Constraints for file size less than 1GB and Jason object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: # Constraints for input key_name capped at 32 chars
                    d[key]=l
            else:
                print("Error: Memory limit exceeded") # Error message 2
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers") # Error message3

            
# Read operation
            
def read(key):
    if key not in d:
        print("Error: Given Key doesn't exist in database. Please enter a valid key") # Error message 4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: # Comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) # To return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("Error: time-to-live of",key,"has expired") # Error message 5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

# Delete operation

def delete(key):
    if key not in d:
        print("Error: Given Key does not exist in database. Please enter a valid key") # Error message 4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: # Comparing the current time with expiry time
                del d[key]
                print("Key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") # Error message 5
        else:
            del d[key]
            print("Key is successfully deleted")

            
            
#I have an additional operation of modify in order to change the value of key before its expiry time if provided

# Modify operation 

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: Given Key does not exist in database. Please enter a valid key") # Error message 6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: time-to-live of",key,"has expired") 
    else:
        if key not in d:
            print("Error: Given Key does not exist in database. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
