--insert a meal plan into database
--EXECUTE [insert_mealplan] <ID>, <date>, <type>
USE [10_MealPlan]
GO
Alter PROCEDURE [insert_mealplan]
(@ID int,
@date datetime,
@type varchar(20))
AS
--if fields are null
if (@ID is null or @date is null or @type is null)
begin
	RAISERROR('ID or date or type cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID already exist
if (EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID))
begin
	RAISERROR('already exist ID', 14, 2);
	RETURN 2; 
end;

--insert the meal plan
INSERT INTO [MealPlan] 
([ID],[date],[type])
VALUES ( @ID, @date, @type)
GO
