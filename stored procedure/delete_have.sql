USE [10_MealPlan]
GO
CREATE PROCEDURE [delete_have]
(@ID int)
AS
--if meal plan ID is null
if (@ID is null)
begin
	RAISERROR('Meal plan ID cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID doesn't exist
if ((NOT EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID)) and (NOT EXISTS (SELECT * FROM [have] WHERE [mealplanID] = @ID)))
begin
	RAISERROR('does not exist ID', 14, 2);
	RETURN 2; 
end;

--delete meal plan
DELETE [have] 
WHERE ([mealplanID] = @ID);
