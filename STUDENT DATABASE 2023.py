import mysql.connector as sql
def Menu():
    c='y'
    while(c=='y' or c=='Y'):
        print()
        print("1. Add")
        print("2. Update")
        print("3. Delete")
        print("4. Search")
        print("5. Display")
        print("6. Quit")
        print()
        ch=int(input("Please enter your choice?"))
        print()
        if ch==1:
            add()
        elif ch==2:
            update()
        elif ch==3:
            delete()
        elif ch==4:
            search()
        elif ch==5:
            display()
        elif ch==6:
            print("Exiting...")
            break
        else:
            print("You have entered an invalid choice!")
        c=input("Do you want to continue?")
        if c=='n':
            print("Operation successful.")
def add():
    import mysql.connector as sql
    con=sql.connect(host="localhost",user="root",password="mysql",database="student_db")
    c=con.cursor()
    grno=int(input("Enter the GR number:"))
    sname=input("Enter the name:")
    sclass=int(input("Enter the class:"))
    sec=input("Enter the section:")
    query="insert into student VALUES({},'{}',{},'{}')".format(grno,sname,sclass,sec)
    c.execute(query)
    con.commit()
def update():
    import mysql.connector as sql
    con=sql.connect(host="localhost",user="root",password="mysql",database="student_db")
    c=con.cursor()
    x=int(input("Enter GR number of student whose name is to be updated:"))
    n=input("Enter new name:")
    c.execute("update student set sname='"+str(n)+"' where grno='"+str(x)+"'")
    con.commit()
def delete():
    import mysql.connector as sql
    con=sql.connect(host="localhost",user="root",password="mysql",database="student_db")
    c=con.cursor()
    x=int(input("Enter GR number of student whose record is to be deleted:"))
    c.execute("delete from student where grno='"+str(x)+"'")
    con.commit()
def search():
    import mysql.connector as sql
    con=sql.connect(host="localhost",user="root",password="mysql",database="student_db")
    c=con.cursor()
    srno=int(input("Enter GR number of student to be searched:"))
    c.execute("select * from student where grno='"+str(srno)+"'")
    results=c.fetchall()
    if c.rowcount!=0:
        for row in results:
            print("GR no=",row[0])
            print("Name=",row[1])
            print("Class=",row[2])
            print("Section=",row[3])
    else:
        print("Student record not found.")
def display():
    import mysql.connector as sql
    con=sql.connect(host="localhost",user="root",password="mysql",database="student_db")
    c=con.cursor()
    c.execute("select * from student")
    d=c.fetchall()
    for i in d:
        print(i)
Menu()


        
    

