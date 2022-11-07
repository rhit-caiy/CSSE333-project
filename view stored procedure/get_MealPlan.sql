--get mealplan of one user
--EXECUTE [get_MealPlan] <Username>
USE [10_MealPlan]
GO
ALTER PROCEDURE [get_MealPlan]
(@Username varchar(50))
AS

Select max(MealPlan.date) as date,count(include.FoodName) as quantity
from MealPlan
join have on have.MealPlanID=MealPlan.ID
left join [include] on [include].MealPlanID=MealPlan.ID
group by have.MealPlanID
having max(have.Username)=@Username