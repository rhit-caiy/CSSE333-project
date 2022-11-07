--get ingredient of food
--EXECUTE [get_foodIngredient] <food name>
USE [10_MealPlan]
GO
CREATE PROCEDURE [get_foodIngredient]
(@foodname varchar(50))
AS
Select * From food
join isIngredientOf on food.name=isIngredientOf.FoodName
join ingredient on ingredient.name=isIngredientOf.IngredientName
where food.name=@foodname