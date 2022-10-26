# -*- coding: utf-8 -*-
#pip install pymssql in console
import pymssql
from tkinter import Canvas,Tk,messagebox,simpledialog
import hashlib

window=Tk()
canvas=Canvas(window,bg="#EEEEEE",width=1400,height=660)#canvas size
window.title("meal plan")

#server, user, password, database
server="titan.csse.rose-hulman.edu"
user="SodaBaseUsercaiy"
password="Password123"
database="10_MealPlan"

# islogin=False
username=""
name=""
userpassword=""

spname=["insert_Person","delete_person","insert_Food","insert_Ingredient","update_name","insert_IsIngredientOf","insert_mealplan","add_mealpan_to_person","delete_mealplan"]
spargs={}

spviewname=["get_Food","get_Ingredient"]
spviewargs={}

spdisplayname=[]#name of sp that access data in database
page=-1

#current plan on page
#0: start page, require login or sign up
#1: main page after log in, able to link to many pages below as well as log out
#2: personal information, merge to page 1
#3: display all food, able to add and then connect food to ingredient
#4: display all ingredient, able to add
#5: show all personal meal plan, able to add or edit meal plan
#6: 
#-1: display most table version

#show content of one table on UI, can only be used for test purpose
def _display(databasetablename,attribute,column):
    r=0#row number used for text coordinate
    canvas.create_text(120*column+40,80,text=databasetablename)
    canvas.create_text(120*column+40,100,text=attribute)
    with pymssql.connect(server,user,password,database) as conn:
        cursor = conn.cursor(as_dict=True)
        cursor.execute('SELECT * FROM '+databasetablename)
        for row in cursor:
            r+=1
            #print(row[attribute],row)
            canvas.create_text(120*column+40,150+20*r,text=row[attribute])
            canvas.update()

#draw grid for database table
def drawgrid(row,col):
    pass

#draw table
def drawtable(table):
    pass

#draw the contents
def draw():
    #use display to display table
    #last argument is column and used for text coordinate
    if page==-1:
        _display("MealPlan","ID",0)
        _display("MealPlan",'date',1)
        _display("MealPlan",'type',2)
        _display("person","Username",3)
        _display("person","name",4)
        _display("food","name",5)
        _display("ingredient","name",6)
        _display("isIngredientOf","FoodName",7)
        _display("isIngredientOf","IngredientName",8)
        _display("have","Username",9)
        _display("have","MealPlanID",10)
        
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
        
        canvas.create_rectangle(1000,500,1100,550)
        canvas.create_text(1050,525,text="go to main page")
    elif page==0:
        canvas.create_text(700,300,text="Meal Plan",font=("Purisa",30))
        
        canvas.create_rectangle(650,400,750,450,fill="#AAAAAA")
        canvas.create_text(700,425,text="log in")
        
        canvas.create_rectangle(650,500,750,550,fill="#AAAAAA")
        canvas.create_text(700,525,text="sign up")
    elif page==1:
        canvas.create_text(700,100,text="Welcome, "+name,font=("Purisa",30))
        
        centerx=200
        centery=300
        width=100
        height=50
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#AAAAAA")
        canvas.create_text(centerx,centery,text="edit username")
        
        centerx=200
        centery=400
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#AAAAAA")
        canvas.create_text(centerx,centery,text="edit password")
        
        centerx=700
        centery=300
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#AAAAAA")
        canvas.create_text(centerx,centery,text="all food")
        
        centerx=700
        centery=400
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#AAAAAA")
        canvas.create_text(centerx,centery,text="all ingredient")
        
        centerx=700
        centery=500
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#AAAAAA")
        canvas.create_text(centerx,centery,text="personal meal plan")
        
        centerx=700
        centery=600
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#AAAAAA")
        canvas.create_text(centerx,centery,text="log out")
        
    elif page==3:#food
        canvas.create_text(100,100,text="food",font=("Purisa",30))
        canvas.create_rectangle(1200,600,1250,650,fill="#AAAAAA")
        canvas.create_text(1225,625,text="menu")
        pass
    elif page==4:#ingredient
        canvas.create_text(100,100,text="ingredient",font=("Purisa",30))
        canvas.create_rectangle(1200,600,1250,650,fill="#AAAAAA")
        canvas.create_text(1225,625,text="menu")
        pass
    elif page==5:#meal plan
        canvas.create_text(100,100,text="meal plan",font=("Purisa",30))
        canvas.create_rectangle(1200,600,1250,650,fill="#AAAAAA")
        canvas.create_text(1225,625,text="menu")
        pass
        

#detect click event on canvas, x and y are integer from up left to bottom right on canvas
def click(coordinate):
    global page,username,name,userpassword
    x=coordinate.x
    y=coordinate.y
    #detect coordinate on canvas and choose event
    
    if page==0:
        if 650<x<750 and 400<y<450:
            #log in
            username=simpledialog.askstring(title="username", prompt="input your username", initialvalue="")
            password1=simpledialog.askstring(title="password", prompt="input your password", initialvalue="")
            password1=hashlib.sha256(password1.encode('utf-8')).hexdigest()
            r=callsp("exist_Person",(username,password1))
            if r and r!=1:
                print("successfully log in with",r)
                page=1
                username=username
                userpassword=password1
                name=r[0]["name"]
            else:
                messagebox.showerror('error',"not exist user or incorrect password")
        elif 650<x<750 and 500<y<550:
            username=simpledialog.askstring(title="username", prompt="input your username", initialvalue="")
            user_name=simpledialog.askstring(title="name", prompt="input your name", initialvalue="")
            password1=simpledialog.askstring(title="password", prompt="input your password", initialvalue="")
            password1=hashlib.sha256(password1.encode('utf-8')).hexdigest()
            if callsp("insert_Person",(username,user_name,password1))==1:
                messagebox.showinfo("successfully sign up","Please log in use account")
    elif page==1:
        if 150<x<250 and 275<y<325:
            newname=simpledialog.askstring(title="password", prompt="input your new name", initialvalue=name)
            if callsp("update_name",(username,newname,userpassword))==1:
                name=newname
        elif 150<x<250 and 375<y<425:
            oldpassword=simpledialog.askstring(title="password", prompt="input your old password", initialvalue="")
            oldpassword=hashlib.sha256(oldpassword.encode('utf-8')).hexdigest()
            if oldpassword!=userpassword:
                messagebox.showerror('error',"password incorrect")
            else:
                newpassword=simpledialog.askstring(title="password", prompt="input new password", initialvalue="")
                newpassword=hashlib.sha256(newpassword.encode('utf-8')).hexdigest()
                if callsp("update_password",(username,oldpassword,newpassword))==1:
                    messagebox.showinfo("success","Password has changed")
        elif 650<x<750:
            if (y-25)//50==5:
                page=3
            elif (y-25)//50==7:
                page=4
            elif (y-25)//50==9:
                page=5
            elif (y-25)//50==11:
                if messagebox.askyesno("log out","Sure to log out?"):
                    page=0
                    username=""
                    name=""
                    userpassword=""
                    
    elif page==-1:#only used for test
        if 100<x<200 and 500<y<550:
            print("insert person")
            personUsername=input("person Username:")
            personName=input("person name:")
            personPassword=input("password:")
            personPassword=hashlib.sha256(personPassword.encode('utf-8')).hexdigest()
            callsp("insert_Person",(personUsername,personName,personPassword))
            
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
            callsp("update_name",(personUsername,newName,personPassword))
            
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
        
        if 1000<x<1100 and 500<y<550:
            page=0
        
    canvas.delete("all")
    draw()
    
#stored procedure, show a dialog if error
def callsp(spname,args):
    print(spname,args)
    try:
        with pymssql.connect(server,user,password,database) as conn:
            with conn.cursor(as_dict=True) as cursor:
                #cursor = conn.cursor(as_dict=True)
                cursor.callproc(spname, args)
                r=[]
                for row in cursor:
                    r.append(row)
                    print(row)
                conn.commit()
                print("finish stored procedure")
                # cnt=cursor.fetchall()
                print(r)
                
                if r:
                    #return query
                    return r
                else:
                    #successfully run without error but no return
                    return 1
    except pymssql._pymssql.DatabaseError as e:
        print("DatabaseError on stored procedure \"",spname,"\" with args",args)
        print(e)
        error=(str(e)+"b\'DB-Lib").split("b\'")[1]
        error=error.split("DB-Lib")[0]
        messagebox.showerror('error',error)
    except pymssql._mssql.MSSQLDatabaseException as e:
        print("MSSQLDatabaseException on stored procedure \"",spname,"\" with args",args)
        error=(str(e)+"b\'DB-Lib").split("b\'")[1]
        error=error.split("DB-Lib")[0]
        messagebox.showerror('error',error)
    except:
        print("Unknown error on stored procedure \"",spname,"\" with args",args)
        messagebox.showerror('error',"error")
    #run with error
    return False
        
#TODO: add more pages and their associated stored procedure
canvas.bind("<Button-1>",click)

draw()
canvas.pack()
window.mainloop()