import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("My Meal Plan")
window.geometry("600x500")

def addFoodToPlan(food, type, ingredient, createdDate):
    plan.insert("",0, text = food, values = (type, ingredient, createdDate))

def addFoodDialog():
    # box = messagebox.askokcancel("Add Food to Meal Plan",)
    add = tk.Toplevel(window)
    add.title("Add a Food to Meal Plan")
    add.geometry("400x100")
    addLable = tk.Label(add, text = "choose the Food You would like to add")
    addLable.grid(column = 0, row = 0)
    str = tk.StringVar(add)
    str.set("Food")
    #todo: load current food available to choose in the database
    #excute('select Name in Food')
    choice = ["pizza", "cake"]
    chooseList = tk.OptionMenu(add,str, *choice)
    chooseList.grid(column = 1, row = 0)
    #todo: add the choosen food to the database
    #call stored Procedre(addFood) here
    ttk.Button(add, text="confirm Addition").grid(column=0, row=1)
    ttk.Button(add, text="Cancel").grid(column=1, row=1)
    add.mainloop()

def editFoodDialog():
    edit = tk.Toplevel(window)
    edit.title("Edit a Food to Meal Plan")
    edit.geometry("400x150")
    chooseEdit = tk.Label(edit, text="Choose the Food you would like to edit")
    chooseEdit.grid(column = 0, row = 0)
    editTo = tk.Label(edit, text="Choose the Food you would like it to be")
    editTo.grid(column = 0, row = 1)
    edit_str = tk.StringVar(edit)
    edit_str.set("Food")
    food_str = tk.StringVar(edit)
    food_str.set("Food")
    #todo: load current food in the user's meal plan
    #execute('select FoodName from have where userName = @userName')
    choice = ["pizza", "cake"]
    chooseList = tk.OptionMenu(edit, edit_str, *choice)
    chooseList.grid(column = 1, row = 0)
    #todo: load available food in database
    #execute('select name from Food')
    food = ["pizza","cake"]
    foodList = tk.OptionMenu(edit, food_str, *food)
    foodList.grid(column = 1, row = 1)
    #todo: add command to edit and delete, connect to stored procedure
    ttk.Button(edit, text = "Update Edit").grid(column = 0 ,row = 2)
    ttk.Button(edit, text = "Delete this Food").grid(column = 1 ,row = 2)
    edit.mainloop()


plan = ttk.Treeview(window)

plan["columns"] = ("type", "ingredient", "createdDate")
plan.column("type", width = 100)
plan.column("ingredient", width = 150)
plan.column("createdDate", width = 100)
plan.heading("type", text = "Food")
plan.heading("ingredient", text = "Ingredient")
plan.heading("createdDate", text = "Created Date")

#test case here
addFoodToPlan("pizza", "lunch",["tomato", "cheese", "bacon"], "2022/10/20" )
addFoodToPlan("cake", "dinner", ["cream", "egg", "sugar", "chocolate"], "2022/10/21")
#todo: load meal plan page
#plans = excute stored procedure get meal plan from user
#for food in plans:
#   type = exccute('select type form food where Name = {food}')
#   ingredient = excute('select ingredientName from iclude where foodName = {food}')
#    time = execute('select timeAdded from mealPlan where foodName = {food}')
#   addFoodToPlan(food, type, ingredient, time)

plan.pack()
ttk.Button(window, text="Add Food To Meal Plan", command=addFoodDialog).pack()
ttk.Button(window, text = "Edit current Food on the Meal Plan", command = editFoodDialog).pack()


window.mainloop()