class Student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.m1 = marks1
        self.m2 = marks2

def accept(ls):
    Name = input("Enter Name: ")
    Rollno = int(input("Enter Rollno: "))
    marks1 = float(input("Enter marks1: "))
    marks2 = float(input("Enter marks2: "))
    ob = Student(Name, Rollno, marks1, marks2)
    ls.append(ob)

def display(ls, ob):
    print("Name   : ", ob.name)
    print("RollNo : ", ob.rollno)
    print("Marks1 : ", ob.m1)
    print("Marks2 : ", ob.m2)
    print("\n")

def search(ls, rn):
    for i in range(len(ls)):
        if(ls[i].rollno == rn):
            return i
    return -1

def delete(ls, rn):
    i = search(ls, rn)
    if(i != -1):
        del ls[i]

def update(ls, rn):
    i = search(ls, rn)
    if(i != -1):
        Name = input("Enter Name: ")
        ls[i].name = Name
        Rollno = int(input("Enter Rollno: "))
        ls[i].rollno = Rollno
        marks1 = float(input("Enter marks1: "))
        ls[i].m1 = marks1
        marks2 = float(input("Enter marks2: "))
        ls[i].m2 = marks2

def show_menu():
    print("1. Input")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")

if __name__ == '__main__':
    ls = []
    while(True):
        show_menu()
        ch = int(input("Enter your choice: "))
        if(ch == 1):
            accept(ls)
        elif(ch == 2):
            for i in range(len(ls)):
                display(ls, ls[i])
        elif(ch == 3):
            rn = int(input("Enter rollno to search: "))
            i = search(ls, rn)
            if(i != -1):
                display(ls, ls[i])
        elif(ch == 4):
            rn = int(input("Enter rollno to delete: "))
            delete(ls, rn)
        elif(ch == 5):
            rn = int(input("Enter rollno to update: "))
            update(ls, rn)
        elif(ch == 6):
            break
        else:
            print("Invalid choice")
