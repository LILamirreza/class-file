import os
import time
names=[]
numbers=[]
grade=[]
classname=[]


def loadData():
    f= open("data.txt",'r')
    #print(f.read())
    #print(f.readline())
    for x in f:
        s=x.replace("\n",'')
        lst=s.split(',')
        names.append(lst[0])
        numbers.append(lst[1])
        grade.append(lst[2])
        classname.append(lst[3])
    f.close()

def saveData():
    f= open("data.txt",'w')
    #print(f.read())
    #print(f.readline())
    for i in range(len(names)):
        f.write(names[i]+","+numbers[i]+","+grade[i]+","+classname[i]+"\n")
    f.close()

def printStudent(i):
    print("Name= "+names[i]+" | Number= "+numbers[i]+" | grade= "+grade[i]+" | classname= "+classname[i] )
def searchByNumber():
    s=input("Enter a number: ")
    for i in range(len(numbers)):
        if numbers[i]==s:
            printStudent(i)
            #break

def searchByClass():
    s=input("Enter a classname: ")
    for i in range(len(classname)):
        if classname[i]==s:
            printStudent(i)
            #break            

def deleteStudent():
    s=input("Enter a number: ")
    for i in range(len(numbers)):
        if numbers[i]==s:
            del numbers[i]
            del names[i]
            del grade[i]
            del classname[i]
            break

def searchByName():
    s=input("Enter a name: ")
    for i in range(len(numbers)):
        if names[i]==s:
            printStudent(i)
            #break

def addContact():
    name=input("Enter name: ")
    number=input("Enter number: ")
    grade=input("Enter grade: ")
    classname=input("Enter classname: ")
    names.append(name)
    numbers.append(number)
    grade.append(grade)
    classname.append(classname)
loadData()

while True:
    os.system('cls')
    print("1.Show All")
    print("2.Search by number")
    print("3.Search by class")
    print("4.Search by name")
    print("5.Add student")
    print("6.Delete student")
    ch=input("Choose an option: ")
    if ch=='1':
        for i in range(len(names)):
            #print("Name= "+names[i]+" | Number= "+numbers[i])
            printStudent(i)
    elif ch=='2':
        searchByNumber()
    elif ch=='3':
        searchByClass()
    elif ch=='4':
        searchByName()
    elif ch=='5':
        addContact()
        saveData()
    elif ch=='6':
        deleteStudent()
    #time.sleep(2)
    input("Enter anything to continue!!!")
