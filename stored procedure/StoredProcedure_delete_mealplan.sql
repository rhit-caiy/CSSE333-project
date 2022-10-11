--delete meal plan from the database
--EXECUTE [delete_MealPlan] <FoodName> <MealPlanID> <amount>
USE [10_MealPlan]
GO
Create PROCEDURE [delete_mealplan]
(@ID int,
@date datetime,
@type varchar(20))
AS
--if meal plan ID is null
if (@ID is null)
begin
	RAISERROR('Meal plan ID cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID doesn't exist
if (NOT EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID))
begin
	RAISERROR('does not exist ID', 14, 2);
	RETURN 2; 
end;

--delete meal plan
DELETE [MealPlan] 
WHERE ([ID] = @ID AND [date] = @date AND [type] = @type);
GO
