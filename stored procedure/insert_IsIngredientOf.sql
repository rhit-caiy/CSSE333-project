--insert isIngredientOf into database
--it should be executed immediately after create food and can not execute any more
--EXECUTE [insert_IsIngredientOf] <food name> <ingredient name> <quantity>
USE [10_MealPlan]
GO
CREATE PROCEDURE [insert_IsIngredientOf]
(@foodname varchar(50),
@ingredientname varchar(50),
@quantity int = 1)
AS
--if either name is null
if (@foodname is null or @ingredientname is null)
begin
	RAISERROR('name cannot be null', 14, 1);
	RETURN 1; 
end;

--if name not exist for food or ingredient
if ((not EXISTS (SELECT * FROM [food] WHERE [name] = @foodname)) or (not EXISTS (SELECT * FROM [ingredient] WHERE [name] = @ingredientname)))
begin
	RAISERROR('not exist name', 14, 1);
	RETURN 2; 
end;

--insert
INSERT INTO [isIngredientOf] 
([FoodName],[IngredientName],[quantity])
VALUES ( @foodname, @ingredientname, @quantity)
GO