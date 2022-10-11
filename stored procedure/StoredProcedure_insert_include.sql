--add food to meal plan in the database
--EXECUTE [update_password] <FoodName> <MealPlanID> <amount>
USE [10_MealPlan]
GO
Create PROCEDURE [add_food_to_mealplan]
(@FoodName varchar(50),
@MealPlanID int,
@amount int)
AS
--if any field is null
If (@FoodName is null or @MealPlanID is null)
Begin
	RAISERROR('Food name or meal plan ID cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the field doesn't exist
IF (NOT EXISTS (SELECT * FROM [food] WHERE name = @FoodName) or NOT EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @MealPlanID))
BEGIN
	RAISERROR('Person username or meal plan ID does not exist in the table.', 14, 2);
	RETURN 2;
END;

--add food to meal plan
INSERT INTO [include] 
([FoodName],[MealPlanID],[amount])
VALUES (@FoodName, @MealPlanID, @amount)
GO
