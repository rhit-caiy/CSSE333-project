--insert an ingredient into database
--EXECUTE [insert_Ingredient] <ingredient name>
USE [10_MealPlan]
GO
CREATE PROCEDURE [insert_Ingredient]
(@name varchar(50))
AS
--if name is null
if (@name is null)
begin
	RAISERROR('ingredient name cannot be null', 14, 1);
	RETURN 1; 
end;

--if name already exist
if (EXISTS (SELECT * FROM [ingredient] WHERE [name] = @name))
begin
	RAISERROR('already exist name', 14, 1);
	RETURN 2; 
end;

--insert
INSERT INTO [ingredient] 
([name])
VALUES ( @name)
GO