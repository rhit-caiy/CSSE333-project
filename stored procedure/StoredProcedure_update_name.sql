--update person name in the database
--EXECUTE [update_name] <Username> <Name>
USE [10_MealPlan]
GO
CREATE PROCEDURE [update_name]
(@Username varchar(50),
@newName varchar(50),
@password varchar(MAX))
AS
--if either name is null
If (@Username is null or @newName is null)
Begin
	RAISERROR('User name or name cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the person doesn't exist
IF (NOT EXISTS (SELECT * FROM [person] WHERE Username = @Username and password = @password))
BEGIN
	RAISERROR('Person username does not exist in the table or password incorrect.', 14, 2);
	RETURN 2;
END;

--update person name
Update [person]
Set [name] = @newName
Where Username = @Username
GO