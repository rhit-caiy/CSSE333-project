--update person password in the database
--EXECUTE [update_password] <Username> <Name>
USE [10_MealPlan]
GO
CREATE PROCEDURE [update_password]
(@Username varchar(50),
@newPassword varchar(50))
AS
--if either name or password is null
If (@Username is null or @newPassword is null)
Begin
	RAISERROR('User name or password cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the person doesn't exist
IF (NOT EXISTS (SELECT * FROM [person] WHERE Username = @Username))
BEGIN
	RAISERROR('Person username does not exist in the table.', 14, 2);
	RETURN 2;
END;

--update person password
Update [person]
Set [password] = @newPassword
Where Username = @Username
GO