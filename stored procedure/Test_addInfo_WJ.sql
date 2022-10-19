Use [10_MealPlan]
Go

--EXECUTE [insert_Person] @Username_1 = 'jul', @Name_2 = 'Le Ju', @Password_3 = '12345';
--Select * From person

--EXECUTE [insert_Ingredient] @name = 'strawberry'
--Select * From ingredient

--EXECUTE [insert_Prefer] @Username = 'jul', @ingredientname  = 'apple';
--Select * From prefer

--EXECUTE [insert_Food] @name = 'strawberry pie', @instruction = 'Strawberry can become to strawberry pie magically.';
--Select * From food

--EXECUTE [insert_IsIngredientOf] @foodname  = 'apple pie', @ingredientname  = 'apple', @quantity = 2;
--Select * From isIngredientOf

--EXECUTE [insert_mealplan] @ID = 2, @date = '2022-10-08', @type = 'Breakfast';
--Select * From MealPlan

--EXECUTE [add_food_to_mealplan] @FoodName = 'apple pie', @MealPlanID = 2, @amount = 2;
--Select * From include

--EXECUTE [add_mealpan_to_person] @Username = 'jul', @MealPlanID = 2, @Quantity = 1;
--Select * From have


--EXECUTE [update_prefer] @Username = 'jul', @newIngredientName = 'strawberry';
--Select * From prefer

--EXECUTE [update_name] @Username = 'jul', @newName = 'Wendy Ju';
--Select * From person

--EXECUTE [update_password] @Username = 'jul', @newPassword = '1234qwer';
--Select * From person


--EXECUTE [delete_mealplan] @ID = 1, @date = '2022-10-10', @type = 'dinner';
--Select * From MealPlan

--EXECUTE [delete_person] @Username = username2, @name = 'Fname2 Lname2', @password = abcdef;
--Select * From person

--Alter table have 
--Add Quantity int;

Go