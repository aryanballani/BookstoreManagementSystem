import mysql.connector  
db=mysql.connector.connect(host="localhost",user="root",password="Devesh123")    
mycur=db.cursor()  
try:
    mycur.execute("create database books")
    print("Database is created....")
except:
    print("The database is existing...")
mycur.execute("use books")
try:
    mycur.execute("create table ibooks(SNO int primary key, NAME char(100), PRICE           decimal(8,2), QTY int, DATE_OF_TRANS date,TRANSACTION char(1))")
    print("IBOOKS table is created")
except:
    print("IBOOKS table exists")


def AddItem():
    no = input("Ino     : ")
    name = input("Name  :  ")
    price=input("Price   :  ")
    dot=input("Date [yyyy-mm-dd] : ")
    qty = input("Quantity : ")
    trans = 'P'
    sql = "insert into ibooks values("+ no +",'" + name + "',"+ price+","+ qty + ",'" +dot+ \
    "',"+"'"+ trans +"')"
    mycur.execute(sql)
    db.commit()

def ViewItem():
    sql="select * from ibooks"
    mycur.execute(sql)
    r=mycur.fetchall()
    cnt=mycur.rowcount
    print("Total number of rows :",cnt)
    for i in r:
        print(i)



def SearchItem():
    ino = input("Ino:")
    sql = "select * from ibooks where sno = " + ino 
    mycur.execute(sql)
    r=mycur.fetchone()
    if r == None:
        print("Item Not found")
    else:
        print("Found...")
        print("Sno           ", r[0])
        print("Item Name     ", r[1])
        print("Price         ",r[2])
        print("Quantity      ", r[3])
        print("Last Transaction Date ", r[4])
        if (r[5] == 'P'):
            Status = "Purchase"
        else:
            Status = "Sale"
        print("Last Transaction ",Status)    


def BuyItem():
    ino =input("Ino:")
    sql = "select count(*) from ibooks where sno = " +ino
    mycur.execute(sql)
    r=mycur.fetchone()
    
    if r == None:
        print("Item is not present")
    else:
        dot = input("Enter new date:")
        qtybuy = input("Enter the quantity:")
        trans="B"
        sql = "select qty from ibooks where sno ="+ino
        mycur.execute(sql)
        r=mycur.fetchone()[0]
        if int(qtybuy)<int(r):
            sql = "update ibooks set qty = qty -" + qtybuy + " ,date_of_trans = '" + dot + \
              "', transaction  = '" +  trans + "' where sno = " + ino 
            mycur.execute(sql)
            db.commit()
            sql = "select qty from ibooks where sno = "+ ino
            mycur.execute(sql)
            r=mycur.fetchone()[0]
            print("Quantity updated in inventory :", r, " for Item No. ", ino)
        elif int(qtybuy)==int(r):
            sql = "delete from ibooks where sno = " + ino
            mycur.execute(sql)
            db.commit
            print("Item removed from inventory")
        else:
            print("this item is not available in sufficient quantity")

def IssueItem():
    ino = input("Ino:")
    sql = "select count(*) from ibooks where sno = " + ino
    mycur.execute(sql)
    r = mycur.fetchone()
    if r == None:
        print("Item ", ino, " is not present")
    else:
        qty = input("Quantity needed   :")
        sql = "select qty from ibooks where sno ="+ino
        mycur.execute(sql)
        r=mycur.fetchone()[0]
        if int(qty) <= int(r):
            dot = input("Enter new date    :")
            trans = 'I'
            sql = "update ibooks set qty = qty -" + qty + ", date_of_trans = '" + dot + "'," +\
             "transaction = '" + trans + "' where sno = " + ino
            mycur.execute(sql)
            db.commit()
            sql = "select qty from ibooks where sno = "+ ino
            mycur.execute(sql)
            r=mycur.fetchone()[0]
            print("Quantity updated in inventory :", r, " for Item No. ", ino)
        else:
            print("this item is not available in sufficient quantity")
    
print("Book Management System")
while True:
    ch=input(" A.Add Item\n V. View Item \n S. Search Item \n B. BuyItem \n I. IssueItem \n Q. Quit\n") 
    if ch in "Aa":
        AddItem()
    elif ch in "Vv":
        ViewItem()
    elif ch in "Ss":
        SearchItem()
    elif ch in "Bb":
        BuyItem()
    elif ch in "Ii":
        IssueItem()
    else:
        break
db.close()
