# -*- coding: utf-8 -*-
#pip install pymssql in console
import pymssql
from tkinter import Canvas,Tk,messagebox
import hashlib

window=Tk()
canvas=Canvas(window,bg="#FFFFFF",width=1400,height=660)#canvas size
window.title("meal plan")

#server, user, password, database
server="titan.csse.rose-hulman.edu"
user="caiy"
l=[9,8,7,6,5,4,3,2,1]
password=str("c")+["x","y","z"][1]+"abcdefg"[2]+str(l[6])+str(l[-1])+"4"+str(2-1)+str(int(1000/190))+str(len(l))
database="10_MealPlan"

spname=["insert_Person","delete_person","insert_Food","insert_Ingredient","update_name","insert_IsIngredientOf","insert_mealplan","add_mealpan_to_person","delete_mealplan"]

spdisplayname=[]#name of sp that access data in database
page=0
#0: start page, require login
#1: main page after log in
#2... : pages to display informations and 

#show content of one table on UI. 
def display(databasetablename,attribute,column):
    r=0#row number used for text coordinate
    canvas.create_text(120*column+40,80,text=databasetablename)
    canvas.create_text(120*column+40,100,text=attribute)
    with pymssql.connect(server,user,password,database) as conn:
        cursor = conn.cursor(as_dict=True)
        #TODO: add stored procedure and display content from that
        cursor.execute('SELECT * FROM '+databasetablename)
        for row in cursor:
            r+=1
            #print(row[attribute],row)
            canvas.create_text(120*column+40,150+20*r,text=row[attribute])
            canvas.update()

#draw grid for database table
def drawgrid():
    pass

#draw the contents
def draw():
    #use display to display table
    #last argument is column and used for text coordinate
    display("MealPlan","ID",0)
    display("MealPlan",'date',1)
    display("MealPlan",'type',2)
    display("person","Username",3)
    display("person","name",4)
    display("food","name",5)
    display("ingredient","name",6)
    display("isIngredientOf","FoodName",7)
    display("isIngredientOf","IngredientName",8)
    display("have","Username",9)
    display("have","MealPlanID",10)
    
    #draw the "buttom" on canvas
    canvas.create_rectangle(110,500,190,550)
    canvas.create_text(150,525,text="add person")
    canvas.create_rectangle(210,500,290,550)
    canvas.create_text(250,525,text="delete person")
    
    canvas.create_rectangle(310,500,390,550)
    canvas.create_text(350,525,text="add food")
    canvas.create_rectangle(410,500,490,550)
    canvas.create_text(450,525,text="add ingredient")
    
    canvas.create_rectangle(510,500,590,550)
    canvas.create_text(550,525,text="edit person name")
    
    canvas.create_rectangle(610,500,690,550)
    canvas.create_text(650,525,text="food ingredient")
    
    canvas.create_rectangle(710,500,790,550)
    canvas.create_text(750,525,text="add meal plan")
    
    canvas.create_rectangle(810,500,890,550)
    canvas.create_text(850,525,text="meal plan to person")
    
    canvas.create_rectangle(910,500,990,550)
    canvas.create_text(950,525,text="delete meal plan")

#detect click event on canvas, x and y are integer from up left to bottom right on canvas
def click(coordinate):
    x=coordinate.x
    y=coordinate.y
    #detect coordinate on canvas and choose event
    #TODO: catch error, use dialog
    
    if 100<x<200 and 500<y<550:
        print("insert person")
        personName=input("person name:")
        personUsername=input("person username:")
        personPassword=input("password:")
        personPassword=hashlib.sha256(personPassword.encode('utf-8')).hexdigest()
        callsp("insert_Person",(personName,personUsername,personPassword))
        
    if 200<x<300 and 500<y<550:
        print("delete person")
        personName=input("person name:")
        personUsername=input("person username:")
        personPassword=input("password:")
        personPassword=hashlib.sha256(personPassword.encode('utf-8')).hexdigest()
        callsp("delete_person",(personName,personUsername,personPassword))
        
    if 300<x<400 and 500<y<550:
        print("add food")
        foodName=input("food name:")
        callsp("insert_Food", (foodName,))
        
    if 400<x<500 and 500<y<550:
        print("add ingredient")
        ingredientName=input("ingredient name:")
        callsp("insert_Food",(ingredientName,))
        
    if 500<x<600 and 500<y<550:
        print("edit person name")
        personUsername=input("person username:")
        newName=input("new name:")
        personPassword=input("password:")
        personPassword=hashlib.sha256(personPassword.encode('utf-8')).hexdigest()
        callsp("update_name",(personUsername,newName,personPassword))#add password
        
    if 600<x<700 and 500<y<550:
        print("add ingredient to food")
        foodName=input("food name:")
        ingredientName=input("ingredient name:")
        quantity=input("quantity (default 1):")
        if not quantity.isnumeric():
            quantity=1
        quantity=int(quantity)
        callsp("insert_IsIngredientOf", (foodName,ingredientName,quantity))
        
    if 700<x<800 and 500<y<550:
        print("add meal plan")
        mealplanID=input("ID:")
        y=input("year:")
        m=input("month:")
        d=input("day:")
        date=y+"-"+m+"-"+d
        t=input("type:")
        callsp("insert_mealplan", (mealplanID,date,t))
        
    if 800<x<900 and 500<y<550:
        print("add meal plan to person")
        mealplanID=int(input("ID:"))
        personUsername=input("person username:")
        quantity=input("quantity:")
        if not quantity.isnumeric():
            quantity=1
        quantity=int(quantity)
        callsp("add_mealpan_to_person", (personUsername,mealplanID,quantity))
        
    if 900<x<1000 and 500<y<550:
        print("delete meal plan")
        mealplanID=input("ID:")
        y=input("year:")
        m=input("month:")
        d=input("day:")
        date=y+"-"+m+"-"+d
        t=input("type:")
        callsp("delete_mealplan", (mealplanID,date,t))
        
    #edit password
        
    canvas.delete("all")
    draw()
    
#stored procedure, show a dialog if error
def callsp(spname,args):
    try:
        with pymssql.connect(server,user,password,database) as conn:
            cursor = conn.cursor(as_dict=True)
            cursor.callproc(spname, args)
            conn.commit()
            print("finish stored procedure")
    except pymssql._pymssql.DatabaseError as e:
        print("DatabaseError on stored procedure \"",spname,"\" with args",args)
        print(e)
        error=str(e).split("b\'")[1]
        error=error.split("DB-Lib")[0]
        messagebox.showerror('error',error)
    except pymssql._mssql.MSSQLDatabaseException as e:
        print("MSSQLDatabaseException on stored procedure \"",spname,"\" with args",args)
        error=str(e).split("b\'")[1]
        error=error.split("DB-Lib")[0]
        messagebox.showerror('error',error)
    except:
        print("Unknown error on stored procedure \"",spname,"\" with args",args)
        messagebox.showerror('error',"error")
        
#TODO: add more stored procedure
#add user account to log in
#add variables to control page
canvas.bind("<Button-1>",click)

draw()
canvas.pack()
window.mainloop()