#!/bin/python3

"""
khaled aldasouki
23-3-2023
"""

import os
import re
import csv
import time
from sys import platform
from time import sleep
"""
Takes in a group name and checks whether or not it exists
return True if the group exists, False if it doesn't
"""
def check_group_exists(group_name):
    group_exists = os.system(f"sudo cat /etc/group | egrep -i -w {group_name} > /dev/null 2>&1")
    if group_exists == 0:
        return True
    return False

"""
creates a group named as the passed string
returns True if the group is created successfully and False if not
"""
def create_group(group_name):
    if os.system(f"sudo groupadd {group_name} > /dev/null 2>&1") == 0:
        return True
    return False

"""
Checks if a phone number is valid using regex
a valid phone number is in the format xxx-xxxx
returns True if valid and false otherwise 
"""
def check_num(num):
    if len(re.findall("\d{3}-\d{4}",num)) == 1:
        return True
    return False

"""
Checks if a office number is valid using regex
a valid office number is in the format xx-xxxx
returns True if valid and false otherwise 
"""
def check_office(num):
    if len(re.findall("\d{2}-\d{4}",num)) == 1:
        return True
    return False

"""
checks whether a name is valid or not using regex
a valid name is a non-empty string that doesn't contain any digits
returns True if the name is valid and False if not
"""
def check_name(name):
    if len(re.findall("\d+",name)) == 0 and name.strip() != "":
        return True
    return False

"""
checks whether a department is valid or not
returns True if valid, False otherwise
"""
def check_dep(department):
    if department.strip() != '':
        return True
    return False

"""
checks whether a group is valid or not
returns True if valid, False otherwise
"""
def check_group(group):
    if group.strip() != '':
        return True
    return False

"""
checks whether or not a user with this anem already exists, and keeps incrementing until it finds the increment of the new user
returns the number (as a string) that should be added to the new user account or an empty string if no number is needed
"""
def check_user(username):
    if os.system(f"sudo cat /etc/passwd | egrep -i -w {username} > /dev/null 2>&1") == 0:
        num = 1
        while True:
            if os.system(f"sudo cat /etc/passwd | egrep -i -w {username + str(num)} > /dev/null 2>&1") == 0:
                num += 1
            else:
                return num
    return ''



"""
takes in a dictionary representing the user, checks it's values and creates a user if everything is valid
returns True once a user is created successfully, and False if any issue was found in the information 
"""
def add_user(user):
        sleep(0.5)
        if len(re.findall('\d{7}',user['EmployeeID'])) == 0:
            print("Failed to add a user                 missing Employee ID")
            return False
        if len(user) < 7:
            print(f"cannot process employee id { user['EmployeeID'] }         insufficient or additional data")
            return False

        id = user['EmployeeID']
        last = user["LastName"]
        first = user["FirstName"]
        office = user["Office"]
        phone = user["Phone"]
        dep = user["Department"]
        group = user["Group"]

        if not check_name(last):
            print(f"cannot process employee id {id}         invalid first name")
            return False
        if not check_name(first):
            print(f"cannot process employee id {id}         invalid last name")
            return False
        if not check_office(office):
            print(f"cannot process employee id {id}         invalid office number")
            return False
        if not check_num(phone):
            print(f"cannot process employee id {id}         invalid phone number")
            return False
        if not check_dep(dep):
            print(f"cannot process employee id {id}         invalid department")
            return False
        if not check_group(group):
            print(f"cannot process employee id {id}         invalid Group")
            return False
        
        if not check_group_exists(group):
            create_group(group)
        
        formated_last = re.sub('\W','',last)
        userid = first[0].lower()+formated_last.lower()
        userid += str(check_user(userid))

        command = f"sudo mkdir -p /home/{dep} >/dev/null 2>&1;sudo useradd -g {group} -m -d /home/{dep}/{userid} -c '{first + ' ' + formated_last}' "

        if group == "office":
            command += "-s /bin/csh "

        command += f"{userid} > /dev/null 2>&1 ;echo {userid}:password | sudo chpasswd {userid} > /dev/null 2>&1; sudo passwd -e {userid} > /dev/null 2>&1"
        if os.system(command) == 0:
            print(f"processed employee id {id}         {userid} added successfully")
            return True

        else:
            print(f"Error occured while adding employee id {id}")
            return False

        
"""
reads a csv file and tries to each user (each row)
"""
def read_users(fileName):
    
        with open(fileName) as file:
            for row in csv.DictReader(file):
                add_user(row)

if __name__ == "__main__":
    
    if platform == "win32":
        print("This tool is made for Linux and cannot be used on Windows.")
        time.sleep(5)
    else:    
        os.system("clear")
        read_users(input("Please enter the csv filepath containing the users you'd like to add: ").strip())   
    
