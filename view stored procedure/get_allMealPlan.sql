--get mealplan of one user
--EXECUTE [get_allMealPlan]
USE [10_MealPlan]
GO
CREATE PROCEDURE [get_allMealPlan]
AS
Select ID From MealPlan
