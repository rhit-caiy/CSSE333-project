--get all food into database
--EXECUTE [get_Food]
USE [10_MealPlan]
GO
CREATE PROCEDURE [get_Food]
AS
Select * From Food