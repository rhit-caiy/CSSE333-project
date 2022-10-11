--delete person from the database
--EXECUTE [delete_person] <Username> <Name> <password>
USE [10_MealPlan]
GO
Create PROCEDURE [delete_person]
(@Username varchar(50),
@name varchar(50),
@password varchar(50))
AS
--if username is null
if (@Username is null or @password is null)
begin
	RAISERROR('Username or password cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID or password doesn't exist
if (NOT EXISTS (Select [Username] From [Person] Where [Username] = @Username) OR NOT EXISTS (Select [password] From [person] Where [password] = @password))
begin
	RAISERROR('does not exist Username or password', 14, 2);
	RETURN 2; 
end;

--delete meal plan
DELETE [person] 
WHERE ([Username] = @Username AND [name] = @name AND [password] = @password);
GO
