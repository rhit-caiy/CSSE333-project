--update person preferernce in the database
--EXECUTE [update_prefer] <Username> <IngredientName>
USE [10_MealPlan]
GO
CREATE PROCEDURE [update_prefer]
(@Username varchar(50),
@newIngredientName varchar(50))
AS
--if either name is null
If (@Username is null or @newIngredientName is null)
Begin
	RAISERROR('User name or ingredient name cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the person doesn't exist
IF (NOT EXISTS (SELECT * FROM person WHERE Username = @Username))
BEGIN
	RAISERROR('Person username does not exist in the table.', 14, 2);
	RETURN 2;
END;

--update person preference
Update [prefer]
Set IngredientName = @newIngredientName
Where Username = @Username
GO