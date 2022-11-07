USE [10_MealPlan]
GO
CREATE PROCEDURE [get_personMealplanID]
(@Username varchar(50))
AS
Select ID From MealPlan
join have on have.MealPlanID=MealPlan.ID
where have.Username=@Username