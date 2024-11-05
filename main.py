import pandas as pd
import sys
from matplotlib import pyplot as plt

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    df = pd.read_csv("idpass.csv")

    df = df.loc[df["username"] == username]
    if df.empty:
        print("INVALID USERNAME")
        return False
    else:
        df = df.loc[df["password"] == password]
        if df.empty:
            print("INVALID PASSWORD")
            return False
        else:
            print("WELCOME USER")
            return True

def showMenu():
    print("MY OWN LIBRARY")
    print("1: Add a new Book")
    print("2: Search a Book")
    print("3: Delete a Book")
    print("4: Display all Books")
    print("5: Add a new Member")
    print("6: Search a Member")
    print("7: Delete a Member")
    print("8: Display all Members")
    print("9: Issue a Book")
    print("10: Return a Book")
    print("11: Display all issued Books")
    print("12: To view a Chart")
    print("13: Exit")

    choice = int(input("Enter choice : "))
    return choice

def addBook():
    book_id = input("Enter book id : ")
    title = input("Enter title : ")
    author = input("Enter author : ")
    publisher = input("Enter publisher : ")
    edition = int(input("Enter edition : "))
    cost = int(input("Enter cost : "))
    category = input("Enter category : ")
    df = pd.read_csv("book.csv")
    n = df["book_id"].count()
    df.loc[n] = [book_id, title, author, publisher, edition, cost, category]
    df.to_csv("book.csv", index=False)
    print("RECORD ADDED SUCCESSFULLY")

def searchBook():
    df = pd.read_csv("book.csv")
    search = input("Enter name to be search : ")
    df3 = df.loc[df["title"] == search]
    if df3.empty:
        print("RECORD NOT FOUND")
    else:
        df2 = df3.to_string(index=False)
        print(df2)

def deleteBook():
    dtitle = input("Enter book name to be deleted  : ")
    df = pd.read_csv("book.csv")
    df = df.drop(df[df["title"] == dtitle].index)
    df.to_csv("book.csv", index=False)
    print("BOOK DELETED")
    print(df)

def displayBook():
    dff = pd.read_csv("book.csv")
    dff = dff.to_string(index=False)
    print(dff)

def addMember():
    member_id = input("Enter member id : ")
    mem_name = input("Enter member name : ")
    cno = int(input("Enter contact no : "))
    books_issued = 0
    df = pd.read_csv("member.csv")
    n = df["member_id"].count()
    df.loc[n] = [member_id, mem_name, cno, books_issued]
    df.to_csv("member.csv", index=False)
    print("RECORD ADDED SUCCESSFULLY")

def searchMember():
    df = pd.read_csv("member.csv")
    search = input("Enter member name to be search : ")
    df3 = df.loc[df["mem_name"] == search]
    if df3.empty:
        print("Record not found")
    else:
        df2 = df3.to_string(index=False)
        print(df2)

def deleteMember():
    member = input("Enter member name to be deleted : ")
    df = pd.read_csv("member.csv")
    # df = df.drop(df[df['mem_name'] == member].index)
    df = df.drop(df.index)
    df.to_csv("member.csv", index=False)
    print("MEMBER DELETED SUCCESSFULLY")
    print(df)

def displayMembers():
    df = pd.read_csv("member.csv")
    df2 = df.to_string(index=False)
    print(df2)

def issueBook():
    bookname = input("Enter book name to issue:")
    df = pd.read_csv("book.csv")
    df3 = df.loc[df["title"] == bookname]
    if df3.empty:
        print("Record not found")
    else:
        member = input("Enter member name : ")
        df = pd.read_csv("member.csv")
        df3 = df.loc[df["mem_name"] == member]
        if df3.empty:
            print("Record not found")
        else:
            issuebook = input("Enter no of issued books :")
            issuedate = input("Enter issued date : ")
            returndate = input("Enter return date : ")
            df = pd.read_csv("issue.csv")
            n = df["book_name"].count()
            df.loc[n] = [bookname, member, issuedate, issuebook, returndate]
            df.to_csv("issue.csv", index=False)
            print("RECORD ADDED SUCCESSFULLY")

def returnBook():
    bookname = input("Enter book name : ")
    df = pd.read_csv("issue.csv")
    df2 = df.loc[df["book_name"] == bookname]
    if df2.empty:
        print("Record not found")
    else:
        membername = input("Enter member name :")
        df = pd.read_csv("issue.csv")
        df3 = df2.loc[df["member_name"] == membername]
        if df3.empty:
            print("MEMBER NOT ISSUED A BOOK")
        else:
            df = df.drop(df3.index)
            df.to_csv("issue.csv", index=False)
            print("BOOK RETURNED")

def displayIssue():
    df = pd.read_csv("issue.csv")
    df2 = df.to_string(index=False)
    print(df2)

def viewChart():
    print('BOOKS AND THEIR VALUES :')
    print('1: BOOK AND THEIR COST ')
    print('2: NO OF BOOKS ISSUED BY MEMBERS')
    choice = int(input('ENter choice : '))
    match choice :
        case 1:
            df = pd.read_csv('book.csv')
            df = df[['title','cost']]
            print(df)
            df.plot('title','cost',kind='bar')
            plt.show()       
        case 2:
            df = pd.read_csv('issue.csv')
            df = df[['member_name','issued_book']]
            print(df)
            df.plot('member_name','issued_book',kind='bar')
            plt.show()       
if login():
    while True:
        ch = showMenu()
        match ch:
            case 1:
                addBook()
            case 2:
                searchBook()
            case 3:
                deleteBook()
            case 4:
                displayBook()
            case 5:
                addMember()
            case 6:
                searchMember()
            case 7:
                deleteMember()
            case 8:
                displayMembers()
            case 9:
                issueBook()
            case 10:
                returnBook()
            case 11:
                displayIssue()
            case 12:
                viewChart()
            case 13:
                exit(0)
            case _:
                print("invalid choice")