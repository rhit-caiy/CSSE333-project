--get food of one user
--EXECUTE [get_personFood] <Username>
USE [10_MealPlan]
GO
CREATE PROCEDURE [get_personFood]
(@Username varchar(50))
AS
Select * From have
join include on have.MealPlanID=include.MealPlanID
join MealPlan on MealPlan.ID=have.MealPlanID
where have.Username=@Username
