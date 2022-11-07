USE [10_MealPlan]
GO
CREATE PROCEDURE [dbo].[get_personMealFood]
(@Username varchar(50),
@mealplanID int)
AS
Select * From have
join include on have.MealPlanID=include.MealPlanID
join MealPlan on MealPlan.ID=have.MealPlanID
where have.Username=@Username and MealPlan.ID=@mealplanID
