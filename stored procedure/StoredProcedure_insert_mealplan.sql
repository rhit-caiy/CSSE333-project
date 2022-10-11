--insert a meal plan into database
--EXECUTE [insert_mealplan] <ID>, <date>, <type>
USE [10_MealPlan]
GO
Create PROCEDURE [insert_mealplan]
(@ID int,
@date datetime,
@type varchar(20))
AS
--if ID is null
if (@ID is null)
begin
	RAISERROR('ID cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID already exists
if (EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID))
begin
	RAISERROR('already exists ID', 14, 2);
	RETURN 2; 
end;

--insert the meal plan
INSERT INTO [MealPlan] 
([ID],[date],[type])
VALUES ( @ID, @date, @type)
GO
