# -*- coding: utf-8 -*-
import pymssql
from tkinter import Canvas,Tk,messagebox,simpledialog,ttk
import tkinter as tk
import hashlib
import time

root=Tk()
canvas=Canvas(root,bg="#EEEEEE",width=1500,height=750)#canvas size
root.title("meal plan")

#server, user, password, database
server="titan.csse.rose-hulman.edu"
user="SodaBaseUsercaiy"
password="Password123"
database="MealPlan10"#"10_MealPlan"

'''
server=input("server:")
user=input("user:")
password=input("password:")
database=input("database:")
'''

#user information
username=""
name=""
userpassword=""

page=0

#current plan on page
#0: start page, require login or sign up
#1: main page after log in, able to link to many pages below as well as log out
#2: personal information, merge to page 1
#3: display all food, able to add and then connect food to ingredient
#4: display all ingredient, able to add
#5: show all personal meal plan, able to add or edit meal plan
#6: 
#-1: display most table version
#
#meal plan: individual window

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
            canvas.create_text(120*column+40,150+20*r,text=row[attribute])
            canvas.update()

#draw grid for database table
def drawgrid(row,col):
    for i in range(int(startx-xwidth/2),int(startx-xwidth/2)+xwidth*(row+1),xwidth):
        canvas.create_line(i,starty-yheight/2,i,starty-yheight/2+col*yheight)
    for i in range(int(starty-yheight/2),int(starty-yheight/2)+yheight*(col+1),yheight):
        canvas.create_line(startx-xwidth/2,i,startx-xwidth/2+row*xwidth,i)

startx=400
starty=100
xwidth=400
yheight=50

rownum=10#how many rows in the display table
startrow=0
totalrow=0
#personal meal plan ID
personalmealplanID=[]

#draw table
def drawtable(table):
    attri=[]
    if type(table)!=list:
        return
    for row in table:
        for key in row.keys():
            if key not in attri:
                attri.append(key)
    x=startx
    y=starty
    i=0
    j=0
    
    for a in attri:
        j=1
        canvas.create_text(x+xwidth*i,y,text=a,font=("Purisa",20))
        for row in table:
            if a=='date':
                canvas.create_text(x+xwidth*i,y+yheight*j,text=row[a].strftime("%Y-%m-%d"))
            else:
                canvas.create_text(x+xwidth*i,y+yheight*j,text=row[a])
            j+=1
        i+=1
    if page==3:
        canvas.create_text(1200,y,text="ingredient",font=("Purisa",20))
        for k in range(len(table)):
            foodingredient=callsp("get_foodIngredient",(table[k]["name"],))
            if type(foodingredient)==list:
                ingredients=str([i["IngredientName"] for i in foodingredient])[1:-1].replace("'","")
            else:
                ingredients="N/A"
            canvas.create_text(1200,y+yheight*k+50,text=str(ingredients))
    if page==5:#meal plan detail
        for k in range(len(table)):
            canvas.create_rectangle(1050,y+yheight*k+30,1150,y+yheight*k+70)
            canvas.create_text(1100,y+yheight*k+50,text="detail")
        for k in range(len(table)):
            canvas.create_rectangle(1200,y+yheight*k+30,1300,y+yheight*k+70)
            canvas.create_text(1250,y+yheight*k+50,text="delete")
    drawgrid(i,j)
        
#draw the contents
def draw():
    global totalrow,personalmealplanID
    #use display to display table
    #last argument is column and used for text coordinate
    canvas.delete("all")
    if page==-1:
        _display("MealPlan","ID",0)
        _display("MealPlan",'date',1)
        #_display("MealPlan",'type',2)
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
        
    if page==0:
        canvas.create_text(700,200,text="Meal Plan",font=("Purisa",30))
        
        canvas.create_rectangle(650,400,750,450,fill="#AAAAAA")
        canvas.create_text(700,425,text="log in")
        
        canvas.create_rectangle(650,500,750,550,fill="#AAAAAA")
        canvas.create_text(700,525,text="sign up")
        
        canvas.create_rectangle(1000,600,1200,700,fill="#AAAAAA")
        canvas.create_text(1100,650,text="developer mode\nwon't be available in final version")
        
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
        
        centerx=200
        centery=600
        canvas.create_rectangle(centerx-width/2,centery-height/2,centerx+width/2,centery+height/2,fill="#FF4040")
        canvas.create_text(centerx,centery,text="delete account")
        
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
        canvas.create_text(200,50,text="food",font=("Purisa",30))
        canvas.create_rectangle(1200,650,1250,700,fill="#AAAAAA")
        canvas.create_text(1225,675,text="menu")
        canvas.create_rectangle(1000,650,1100,700,fill="#AAAAAA")
        canvas.create_text(1050,675,text="add food")
        canvas.create_rectangle(800,650,900,700,fill="#AAAAAA")
        canvas.create_text(850,675,text="edit food name instruction")
        canvas.create_rectangle(600,650,700,700,fill="#AAAAAA")
        canvas.create_text(650,675,text="edit food ingredient")
        table=callsp("get_Food",())
        if type(table)==list:
            totalrow=len(table)
            drawtable(table[startrow:startrow+rownum])
            
        
    elif page==4:#ingredient
        canvas.create_text(200,50,text="ingredient",font=("Purisa",30))
        canvas.create_rectangle(1200,650,1250,700,fill="#AAAAAA")
        canvas.create_text(1225,675,text="menu")
        canvas.create_rectangle(1000,650,1100,700,fill="#AAAAAA")
        canvas.create_text(1050,675,text="add ingredient")
        table=callsp("get_Ingredient",())
        if type(table)==list:
            totalrow=len(table)
            drawtable(table[startrow:startrow+rownum])
        
    elif page==5:#meal plan
        canvas.create_text(200,50,text="my meal plan",font=("Purisa",30))
        canvas.create_rectangle(1200,650,1250,700,fill="#AAAAAA")
        canvas.create_text(1225,675,text="menu")
        canvas.create_rectangle(1000,650,1100,700,fill="#AAAAAA")
        canvas.create_text(1050,675,text="add meal plan")
        table=callsp("get_Mealplan",(username,))
        if type(table)==list:
            totalrow=len(table)
            drawtable(table[startrow:startrow+rownum])
            personalmealplanID=[i["ID"] for i in callsp("get_personMealplanID",(username,))]
            #print(personalmealplanID)
            
    if page==3 or page==4 or page==5:
        canvas.create_text(200,650,text="←",font=("Purisa",30))
        canvas.create_text(300,650,text="→",font=("Purisa",30))
        canvas.create_text(100,650,text=str(startrow)+"-"+str(startrow+rownum)+"/"+str(totalrow))

    
#detect click event on canvas, x and y are integer from up left to bottom right on canvas
def click(coordinate):
    global page,username,name,userpassword,startrow
    x=coordinate.x
    y=coordinate.y
    #detect coordinate on canvas and choose event
    
    if page==0:
        if 650<x<750 and 400<y<450:
            #log in
            username=simpledialog.askstring(title="username", prompt="input your username", initialvalue="")
            password1=simpledialog.askstring(title="password", prompt="input your password", initialvalue="",show="*")
            password1=hashlib.sha256(password1.encode('utf-8')).hexdigest()
            r=callsp("exist_Person",(username,password1))
            if r and r!=1:
                #print("successfully log in with",r)
                page=1
                username=username
                userpassword=password1
                name=r[0]["name"]
            else:
                messagebox.showerror('error',"not exist user or incorrect password")
        elif 650<x<750 and 500<y<550:
            username=simpledialog.askstring(title="username", prompt="input your username", initialvalue="")
            user_name=simpledialog.askstring(title="name", prompt="input your name", initialvalue="")
            password1=simpledialog.askstring(title="password", prompt="input your password", initialvalue="",show="*")
            password1=hashlib.sha256(password1.encode('utf-8')).hexdigest()
            if callsp("insert_Person",(username,user_name,password1))==1:
                messagebox.showinfo("successfully sign up","Please log in use account")
        
        elif 1000<x<1200 and 600<y<700:
            page=-1
        
    elif page==1:
        startrow=0
        if 150<x<250 and 275<y<325:
            newname=simpledialog.askstring(title="password", prompt="input your new name", initialvalue=name)
            if callsp("update_name",(username,newname,userpassword))==1:
                name=newname
        elif 150<x<250 and 375<y<425:
            oldpassword=simpledialog.askstring(title="password", prompt="input your old password", initialvalue="",show="*")
            oldpassword=hashlib.sha256(oldpassword.encode('utf-8')).hexdigest()
            if oldpassword!=userpassword:
                messagebox.showerror('error',"password incorrect")
            else:
                newpassword=simpledialog.askstring(title="password", prompt="input new password", initialvalue="",show="*")
                newpassword=hashlib.sha256(newpassword.encode('utf-8')).hexdigest()
                if callsp("update_password",(username,oldpassword,newpassword))==1:
                    messagebox.showinfo("success","Password has changed")
        elif 150<x<250 and 575<y<625:
            password1=simpledialog.askstring(title="delete account", prompt="input your password to delete account", initialvalue="",show="*")
            password1=hashlib.sha256(password1.encode('utf-8')).hexdigest()
            if password1!=userpassword:
                messagebox.showerror('error',"password incorrect")
            elif messagebox.askyesno("delete","Sure to delete account?\nThe account can't be found back"):
                if callsp("delete_person",(username,name,password1))==1:
                    page=0
                    username=""
                    name=""
                    userpassword=""
                
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
    elif page==3:
        if 1200<x<1250 and 650<y<700:
            page=1
        elif 1000<x<1100 and 650<y<700:
            foodName=simpledialog.askstring(title="create food", prompt="input name of food", initialvalue="")
            foodInstruction=simpledialog.askstring(title="create food", prompt="input food instruction", initialvalue="")
            if callsp("insert_Food", (foodName,foodInstruction)):
                #add ingredient to food
                addfoodingredient(foodName)
        elif 800<x<900 and 650<y<700:
            editFoodDialog()
        elif 600<x<700 and 650<y<700:
            foodName=simpledialog.askstring(title="edit ingredient", prompt="input name of food", initialvalue="")
            foodNameList=[i["name"] for i in callsp("get_Food",())]
            if foodName in foodNameList:
                addfoodingredient(foodName)
                draw()
            else:
                messagebox.showerror('error',"food not exist")
            
    elif page==4:
        if 1200<x<1250 and 650<y<700:
            page=1
        elif 1000<x<1100 and 650<y<700:
            ingredientName=simpledialog.askstring(title="create ingredient", prompt="input name of ingredient", initialvalue="")
            callsp("insert_Ingredient", (ingredientName,))
            
    elif page==5:
        #print(x,y)
        if 1200<x<1250 and 650<y<700:
            page=1
        elif 1000<x<1100 and 650<y<700:
            mealplanIDs=callsp("get_allMealPlan",())
            print(mealplanIDs)
            if type(mealplanIDs)==list:
                mealplanIDs=[i['ID'] for i in mealplanIDs]
                newID=max(mealplanIDs)+1
            else:
                mealplanIDs=[]
                newID=1
            year=simpledialog.askstring(title="new mealplan", prompt="input year", initialvalue=time.strftime("%Y", time.localtime()))
            month=simpledialog.askstring(title="new mealplan", prompt="input month", initialvalue=time.strftime("%m", time.localtime()))
            day=simpledialog.askstring(title="new mealplan", prompt="input day", initialvalue=time.strftime("%d", time.localtime()))
            if year and month and day:
                date=year+"-"+month+"-"+day
                if callsp("insert_mealplan", (newID,date)):
                    callsp("add_mealpan_to_person", (username,newID,1))
                
        elif 1050<x<1150:
            #meal plan detail 
            for i in range(rownum):
                if i+startrow>totalrow:
                    break
                if 130+i*yheight<y<170+i*yheight:
                    canvas.create_rectangle(1080,140+i*yheight,1120,160+i*yheight)
                    try:
                        print("meal plan id is",personalmealplanID[i+startrow])
                        generateMealPlan(username,personalmealplanID[i+startrow])
                    except:
                        pass
        elif 1200<x<1300:
            #delete
            for i in range(rownum):
                if i+startrow>=totalrow:
                    break
                if 130+i*yheight<y<170+i*yheight:
                    if messagebox.askyesno("delete mealplan","Sure to delete?"):
                        callsp("delete_have", (personalmealplanID[i+startrow],))
                    
                    
    if page==3 or page==4 or page==5:
        if 170<x<230 and 600<y<700:
            print("left")
            if startrow>0:
                startrow-=rownum
        if 270<x<330 and 600<y<700:
            print("right")
            if startrow+rownum<totalrow:
                startrow+=rownum
    
    if page==-1:#only used for test
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
            callsp("insert_Ingredient",(ingredientName,))
            
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
        
    draw()
    
#stored procedure, show a dialog if error
def callsp(spname,args):
    #print(spname,args)
    try:
        with pymssql.connect(server,user,password,database) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.callproc(spname, args)
                r=[]
                for row in cursor:
                    r.append(row)
                conn.commit()
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

def addfoodingredient(foodName):
    def move():
        a=lb.get("active")
        lb.delete("active")
        lb2.insert("end",a)
    def remove():
        a=lb2.get("active")
        lb2.delete("active")
        lb.insert("end",a)
    def confirm():
        callsp("delete_food_ingredient",(foodName,))
        for i in range(lb2.size()):
            try:
                callsp("insert_IsIngredientOf",(foodName,lb2.get(i),1))
            except:
                pass
        window1.destroy()
        draw()
    def addI():
        ingredientName=simpledialog.askstring(title="create ingredient", prompt="input name of ingredient", initialvalue="")
        if callsp("insert_Ingredient", (ingredientName,)):
            lb2.insert("end",ingredientName)
        
    window1 = tk.Tk()
    window1.title("add ingredient of "+foodName)
    window1.geometry("400x600")
    lb=tk.Listbox(window1)
    lb2=tk.Listbox(window1)
    ingredientList = callsp("get_Ingredient",())
    if type(ingredientList)==list:
        ingredientList=[i["name"] for i in ingredientList]
    else:
        ingredientList=[]
    foodingredient = callsp("get_foodIngredient", (foodName,))
    if type(foodingredient)==list:
        foodingredient=[i["IngredientName"] for i in foodingredient]
    else:
        foodingredient=[]
    for i in ingredientList:
        if i in foodingredient:
            lb2.insert("end",i)
        else:
            lb.insert("end",i)
        
    tk.Label(window1,text="unselected ingredient").grid(row=0,column=0)
    tk.Label(window1,text="selected ingredient").grid(row=0,column=1)
    lb.grid(row=1,column=0)
    lb2.grid(row=1,column=1)
    
    button=tk.Button(window1,text="add",command=move)
    button.grid(row=2,column=0)
    button=tk.Button(window1,text="remove",command=remove)
    button.grid(row=2,column=1)
    
    button=tk.Button(window1,text="confirm",command=confirm)
    button.grid(row=3)
    button=tk.Button(window1,text="add ingredient",command=addI)
    button.grid(row=4)
    
    window1.mainloop()


def generateMealPlan(username,mealplanID):
    #print("generate meal plan for",username,mealplanID)
    def loadFoodToPlan(food, type, ingredient, createdDate):
        plan.insert("",0, text = food, values = (type, ingredient, createdDate))

    def updatePlan():
        for item in plan.get_children():
            plan.delete(item)
        allfood = callsp("get_personMealFood", (username,mealplanID))
        if allfood and allfood != 1:
            for food in allfood:
                foodingredient = callsp("get_foodIngredient", (food["FoodName"],))
                if type(foodingredient)==list:
                    ingredients = [i["IngredientName"] for i in foodingredient]
                else:
                    ingredients=["N/A"]
                loadFoodToPlan(food["FoodName"], food["type"], ingredients, food["date"].strftime("%Y-%m-%d"))

        
    def addFoodDialog():
        def addToPlan():
            # print(inputFood.get())
            if callsp("add_food_to_mealplan", (inputFood.get(), mealplanID, inputType.get())):
                updatePlan()
                add.destroy()
        def cancel():
            add.destroy()

        add = tk.Toplevel(window)
        add.title("Add a Food to Meal Plan")
        add.geometry("400x100")
        
        typeLable = tk.Label(add, text="select a type")
        typeLable.grid(column=0, row=0)
        inputType = tk.StringVar(add)
        inputType.set("Type")
        
        types = ["breakfast", "lunch", "dinner", "brunch", "tea","supper","snack","picnic", "other"]
        typeList = tk.OptionMenu(add, inputType, *types)
        typeList.grid(column = 1, row = 0)
        

        addLable = tk.Label(add, text = "choose the Food You would like to add")
        addLable.grid(column = 0, row = 1)
        inputFood = tk.StringVar(add)
        inputFood.set("Food")
        foodList = callsp("get_Food",())
        choice = []
        for food in foodList:
            choice.append(food["name"])
        chooseList = tk.OptionMenu(add,inputFood, *choice)
        chooseList.grid(column = 1, row = 1)
        ttk.Button(add, text="confirm Addition", command = addToPlan).grid(column=0, row=2)
        ttk.Button(add, text="Cancel", command = cancel).grid(column=1, row=2)
        add.mainloop()

    def mpeditFoodDialog():
        def editFood():
            callsp("editFoodOnPlan",(mealplanID, inputFood.get(), inputChangeTo.get(),))
            updatePlan()
            edit.destroy()
        def deleteFood():
            callsp("deleteFoodOnPlan",(username,mealplanID, inputFood.get(),))
            updatePlan()
            edit.destroy()
        edit = tk.Toplevel(window)
        edit.title("Edit a Food to Meal Plan")
        edit.geometry("400x150")
        chooseEdit = tk.Label(edit, text="Choose the Food you would like to edit")
        chooseEdit.grid(column = 0, row = 0)
        editTo = tk.Label(edit, text="Choose the Food you would like it to be")
        editTo.grid(column = 0, row = 1)
        inputFood = tk.StringVar(edit)
        inputFood.set("Food")
        inputChangeTo = tk.StringVar(edit)
        inputChangeTo.set("Food")
        userFood = callsp("get_personMealFood", (username,mealplanID))
        choice = []
        for food in userFood:
            choice.append(food["FoodName"])
        chooseList = tk.OptionMenu(edit, inputFood, *choice)
        chooseList.grid(column = 1, row = 0)
        changeTo = []
        food = callsp("get_Food",())
        for item in food:
            changeTo.append(item["name"])
        foodList = tk.OptionMenu(edit, inputChangeTo, *changeTo)
        foodList.grid(column = 1, row = 1)
        ttk.Button(edit, text = "Update Edit",command = editFood).grid(column = 0 ,row = 2)
        ttk.Button(edit, text = "Delete this Food", command = deleteFood).grid(column = 1 ,row = 2)
        edit.mainloop()


    def createFoodDialog():
        foodName=simpledialog.askstring(title="create food", prompt="input name of food", initialvalue="")
        foodInstruction=simpledialog.askstring(title="create food", prompt="input food instruction", initialvalue="")
        if callsp("insert_Food", (foodName,foodInstruction)):
            #add ingredient to food
            addfoodingredient(foodName)
        # def notContain(list, item):
        #     for i in list:
        #         if i == item:
        #             return False
        #     return True

        # def addIngredient(col, list):
        #     if notContain(list, inputIngredient.get()):
        #         addedIngredient = tk.Label(createFood, text = inputIngredient.get())
        #         addedIngredient.grid(column = col[0], row = 2)
        #         col[0] += 1
        #         list.append(inputIngredient.get())

        # def createFood(food, ingredient, instruction):
        #     callsp("",(food, instruction))#create a food name with instruction
        #     callsp("",(food, ingredient)) ##add the information into include relation table

        # createFood = tk.Toplevel(window)
        # createFood.title("create food")
        # createFood.geometry("400x200")
        # foodName = tk.Label(createFood, text="foodName")
        # foodName.grid(column = 0, row = 0)
        # inputFoodName = tk.Entry(createFood)
        # inputFoodName.grid(column = 1, row = 0)
        # availableIngredient = []
        # ingredientList = callsp("get_Ingredient",())
        # for item in ingredientList:
        #     availableIngredient.append(item["name"])
        # inputIngredient = tk.StringVar()
        # inputIngredient.set("ingredient")
        # chooseIngredientList = tk.OptionMenu(createFood, inputIngredient, *availableIngredient)
        # col = [0]
        # chosenIngredient = []
        # chooseIngredientList.grid(column = 0, row = 1)
        # instructionLabel = tk.Label(createFood, text = "instruction")
        # instructionLabel.grid(column = 0, row = 3)
        # inputInstruction = tk.Entry(createFood)
        # inputInstruction.grid(column = 1, row = 3)
        # tk.Button(createFood, text = "add", command = lambda:addIngredient(col, chosenIngredient)).grid(column = 1, row = 1)
        # tk.Button(createFood, text = "create", command = lambda: createFood(inputFoodName,chosenIngredient, inputInstruction)).grid(column = 1, row = 4)

    def addfoodingredient(foodName):
        def move():
            a=lb.get("active")
            lb.delete("active")
            lb2.insert("end",a)
        def remove():
            a=lb2.get("active")
            lb2.delete("active")
            lb.insert("end",a)
        def confirm():
            callsp("delete_food_ingredient",(foodName,))
            for i in range(lb2.size()):
                try:
                    callsp("insert_IsIngredientOf",(foodName,lb2.get(i),1))
                except:
                    pass
            window1.destroy()
            updatePlan()
        def addI():
            ingredientName=simpledialog.askstring(title="create ingredient", prompt="input name of ingredient", initialvalue="")
            if callsp("insert_Ingredient", (ingredientName,)):
                lb2.insert("end",ingredientName)
            
        window1 = tk.Tk()
        window1.title("add ingredient of "+foodName)
        window1.geometry("400x600")
        lb=tk.Listbox(window1)
        lb2=tk.Listbox(window1)
        ingredientList = callsp("get_Ingredient",())
        ingredientList=[i["name"] for i in ingredientList]
        foodingredient = callsp("get_foodIngredient", (foodName,))
        if type(foodingredient)==list:
            foodingredient=[i["IngredientName"] for i in foodingredient]
        else:
            foodingredient=[]
        for i in ingredientList:
            if i in foodingredient:
                lb2.insert("end",i)
            else:
                lb.insert("end",i)
            
        tk.Label(window1,text="unselected ingredient").grid(row=0,column=0)
        tk.Label(window1,text="selected ingredient").grid(row=0,column=1)
        lb.grid(row=1,column=0)
        lb2.grid(row=1,column=1)
        
        button=tk.Button(window1,text="add",command=move)
        button.grid(row=2,column=0)
        button=tk.Button(window1,text="remove",command=remove)
        button.grid(row=2,column=1)
        
        button=tk.Button(window1,text="confirm",command=confirm)
        button.grid(row=3)
        button=tk.Button(window1,text="add ingredient",command=addI)
        button.grid(row=4)
        
        window1.mainloop()



    def createIngredientDialog():
        # createIngredient = tk.Toplevel(window)
        # createIngredient.title("create ingredients")
        # createIngredient.geometry("300x200")
        ingredientName=simpledialog.askstring(title="create ingredient", prompt="input name of ingredient", initialvalue="")
        callsp("insert_Ingredient", (ingredientName,))
        
    def editFoodIngredient():
        foodName=simpledialog.askstring(title="edit ingredient", prompt="input name of food", initialvalue="")
        foodNameList=[i["name"] for i in callsp("get_Food",())]
        if foodName in foodNameList:
            addfoodingredient(foodName)
            generateMealPlanMain()
            updatePlan()
        else:
            messagebox.showerror('error',"food not exist")
    
    window = tk.Tk()
    window.title("My Meal Plan")
    window.geometry("700x500")
    
    plan = ttk.Treeview(window)

    plan["columns"] = ("type", "ingredient", "createdDate")
    plan.column("type", width = 100)
    plan.column("ingredient", width = 150)
    plan.column("createdDate", width = 130)
    plan.heading("type", text = "type")
    plan.heading("ingredient", text = "Ingredient")
    plan.heading("createdDate", text = "Plan Date")
    
    def generateMealPlanMain():
        allfood=callsp("get_personMealFood",(username,mealplanID))
        if type(allfood)==list:
            for food in allfood:
                #print(food)
                foodingredient=callsp("get_foodIngredient",(food["FoodName"],))
                if type(foodingredient)==list:
                    ingredients=[i["IngredientName"] for i in foodingredient]
                else:
                    ingredients=["N/A"]
                loadFoodToPlan(food["FoodName"],food["type"],ingredients,food["date"].strftime("%Y-%m-%d"))
        plan.pack()
        ttk.Button(window, text="Add Food To Meal Plan", command=addFoodDialog).pack()
        ttk.Button(window, text = "Edit current Food on the Meal Plan", command = mpeditFoodDialog).pack()
        ttk.Button(window, text = "create food",command = createFoodDialog).pack()
        ttk.Button(window, text = "create ingredient",command = createIngredientDialog).pack()
        ttk.Button(window, text = "edit an existing food",command = editFoodDialog).pack()
        ttk.Button(window, text = "edit ingredient of food",command = editFoodIngredient).pack()
    generateMealPlanMain()
    window.mainloop()

def editFoodDialog():
    def editFoodOnClick(foodName, newFoodName, newInstruction):
        # print(foodName, newFoodName, newInstruction)
        callsp("edit_food", (foodName, newFoodName, newInstruction))
        dialog.destroy()

    def deleteFoddOnClick(foodName):
        callsp("delete_food", (foodName,))
        dialog.destroy()


    dialog = tk.Toplevel()
    dialog.geometry("500x150")

    # instruction label - food
    foodLabel = tk.Label(dialog, text = "chose a food that you would like to edit")
    foodLabel.grid(column = 0 , row = 0)

    # option menu
    editableFood = callsp("getFoodNotOnPlan", ())
    chooseList = [" "]
    if type(editableFood)!=list:
        editableFood=[]
    else:
        chooseList=[]
    for item in editableFood:
        chooseList.append(item["name"])
    inputFoodName = tk.StringVar(dialog, "food")
    chooseFoodMenu = tk.OptionMenu(dialog, inputFoodName, *chooseList)
    chooseFoodMenu.grid(column = 1, row = 0)

    # instruction label - newFood
    newFoodLabel = tk.Label(dialog, text = "new foodName")
    newFoodLabel.grid(column = 0, row = 1)

    #input new food name
    inputNewFoodName = tk.Entry(dialog)
    inputNewFoodName.grid(column = 1, row = 1)

    newInstructionLabel = tk.Label(dialog, text = "new instruction")
    newInstructionLabel.grid(column = 0, row = 2)

    inputNewInstruction = tk.Entry(dialog)
    inputNewInstruction.grid(column = 1, row =2)

    tk.Button(dialog, text = "edit", command = lambda: editFoodOnClick(inputFoodName.get(), inputNewFoodName.get(), inputNewInstruction.get())).grid(column = 0, row = 3)
    tk.Button(dialog, text = "delete",command = lambda: deleteFoddOnClick(inputFoodName.get())).grid(column = 1, row = 3)


canvas.bind("<Button-1>",click)

draw()
canvas.pack()
root.mainloop()