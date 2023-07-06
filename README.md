# Linux User Adder
A script that automates adding users to a Linux machine while checking information and conditions

## NOTICE 
This script was written for Linux machines using CentOS and may run differently on other distros.
Furthermore the CSV file is expected to have <b> at least </b> the following columns (case sensitive): EmployeeID, LastName, FirstName, Office, Phone, Department, Group

## PROJECT REQUIREMENTS

1. The CSV file contains a header line defining the fields 
2. The users should have a default group as indicated in the File
3. Unique user names are created as first initial followed by the last name (e.g., John Smith would be assigned the user name 'jsmith').
4. Duplicate names are appended a number, to the account name. For example, jsmith, jsmith1, jsmith2, and so forth.
5. The script handles embedded special characters such as in "O'Donnell"
6. The script handles missing or incorrect information in the fields (a file with a field that is not populated or has incorrect data? The script handles this possibility by reporting it to the user.
7. The user's home directory is located in /home/department, where department is the user's department,
8. Any member assigned to the “office” group is assigned “csh” (C shell) as their default shell, everyone else is assigned
the Borne Again Shell, or Bash as the default.
9. The script detects incorrect data (full name in the CSV file is '555-1212', the person doing data entry made mistakes, etc.) adn reports it to the user.
10. The default password is “password” for each new user.
11. The password expires the first time the user logs in so that they must change it.
12. Each record in the CSV file indicates the default group for the corresponding user, and creates it if it doesn't exist.

## CONDITIONS AND CHECKS 

1. Valid phone numbers are in the format xxx-xxxx
2. Valid office numbers are in the format xx-xxxx
3. Valid names are non-empty strings with no digits
4. Valid departments and groups are non-empty strings
   
## USAGE
1. Run the script using a shell or an IDE
2. Enter the csv file name or path
3. wait for the program to finish running, while monitoring the output for any issues or reports

   
