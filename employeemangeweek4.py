print('----------Employee Management System----------')

my_list= []

def func():
    global x
    print(x)
    x = 'my_list.count'
    print(x)
print('\n     There are '+ str(len(my_list))+' employees in the system.')
print('---------------------------------------------')

while True:
    name = input("\nEnter New Employee Name ") 
    ssn = input("Enter New Employee Social Security Number: ")
    phone = input("Enter New Employee phone number: ")
    email = input("Enter New email : ")
    salary = input("Enter New salary: ")
    i =("-")

    a= "-----" + name, "SSN: " + ssn,"Phone: " + phone,"Email: " + email,"Salary: " + salary
    print()
            
    my_list.append(a)
    
    a1=(input('\nAdd another employee: y or n: '))
    if a1 =='n':
        print('Thank you')
        break
   
a2 = input('\nWould you like to view employees: y or n: ')
if a2 == 'y':
    print(*my_list)
    
def func():
    global x
    print(x)
    x = 'my_list.count'
    print(x)
    
a3 = input('\nWould you like to view number of employees: y or n: ')
if a3 == 'n' :
    print('\nThank you')
else:
    print('\nThere are '+ str(len(my_list))+' employees in the system.')


a4 = input('\nSearch by ssn#: ')
for employee in my_list:
    if a4 in employee:
        print('\n',employee)
            
for employee in my_list: 
    input('Edit Employee: y or n: ')
    if 'y':
        name = input("\nEnter Employee Name ") 
        ssn = input("Enter Employee Social Security Number: ")
        phone = input("Enter Employee phone number: ")
        email = input("Enter email : ")
        salary = input("Enter salary: ")
        a7 = "-----" + name, "SSN: " + ssn,"Phone: " + phone,"Email: " + email,"Salary: " + salary
        my_list.append(a7)
        
    else:
        print('Thank You')
    break

f = open('myfile.txt', 'w')
f.write(str(my_list))
f.close()

f = open('myfile.txt', 'r')
if f.mode == 'r':
    content = f.read()
    print()
f.close()

file = open('textd.txt', 'r')
employee = file.readlines()
my_list.extend(employee)
file.close()
print()







