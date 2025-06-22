# 1.  Create a class Emp (eid,ename,basic) 
# 2.  WAP a menu driven program to perform following operations using files : 
    # a.  Add a record 
    # b.  Search for a record using id 
    # c.  Delete a record using id 
    # d.  Edit a record using id. 
    # e.  Display all records. 

import pickle

class emp:
    def __init__(self, eid=0, ename="not given", basic=0):
        self.eid = eid
        self.ename = ename
        self.basic = basic
    
    def display(self):
        print("---------------------------------")
        print("Employee id = ", self.eid)
        print("Name = ", self.ename)
        print("Basic Salary = ", self.basic)
        print("---------------------------------")

def write_file(e_list):
    with open("emp.bin", "wb") as ef:
        pickle.dump(e_list, ef)

def read_file():
    try:
        with open("emp.bin", "rb") as ef:
            return pickle.load(ef)
    except:
        return []

e = read_file()

while True:
    print("\n1. Add a record\n2. Search a record\n3. Delete a record\n4. Edit a record\n5. Display all records\n0. Exit")
    ch = int(input("Enter your choice = "))

    if ch == 1:
        eid = int(input("Enter the employee id = "))
        en = input("Enter the name = ")
        eb = int(input("Enter the basic salary = "))
        e.append(emp(eid, en, eb))

    elif ch == 2:
        eid = int(input("Enter the employee id to search = "))
        found = False
        for emp_obj in e:
            if emp_obj.eid == eid:
                emp_obj.display()
                found = True
                break
        if not found:
            print("Employee not found.")

    elif ch == 3:
        eid = int(input("Enter the employee id to delete = "))
        found = False
        for i in range(len(e)):
            if e[i].eid == eid:
                del e[i]
                print("Employee deleted.")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif ch == 4:
        eid = int(input("Enter the employee id to edit = "))
        found = False
        for emp_obj in e:
            if emp_obj.eid == eid:
                print("1. Edit ID\n2. Edit Name\n3. Edit Basic Salary")
                ec = int(input("Enter your choice = "))
                if ec == 1:
                    emp_obj.eid = int(input("Enter new ID = "))
                elif ec == 2:
                    emp_obj.ename = input("Enter new name = ")
                elif ec == 3:
                    emp_obj.basic = int(input("Enter new salary = "))
                else:
                    print("Invalid choice.")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif ch == 5:
        if not e:
            print("No employee records.")
        for emp_obj in e:
            emp_obj.display()

    elif ch == 0:
        write_file(e)
        print("Thank you! Data saved.")
        break

    else:
        print("Invalid choice.")