USE [10_MealPlan]
GO

create proc [delete_food_ingredient](@foodName varchar(50))
as

begin
	delete from isIngredientOf where FoodName = @foodName
end