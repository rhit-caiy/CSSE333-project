--exist user?
--EXECUTE [exist_Person] <name> <password>
USE [10_MealPlan]
GO
CREATE PROCEDURE [exist_Person]
(@Username varchar(50),
@Password varchar(MAX))
AS
Select * From Person where Username=@Username and Password=@Password