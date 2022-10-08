--insert a person into database
--EXECUTE [insert_Person] <Username>,<Name>,<Password>
CREATE PROCEDURE [insert_Person]
(@Username_1 varchar(50),
@Name_2 varchar(50)=null,
@Password_3 varchar(50))
AS
--if username or password of key value is null
if (@Username_1 is null or @Password_3 is null)
begin
	RAISERROR('username and password cannot be null', 14, 1);
	RETURN 1; 
end;

--if username already exist
if (EXISTS (SELECT * FROM [person] WHERE Username = @Username_1))
begin
	RAISERROR('already exist username', 14, 1);
	RETURN 2; 
end;

--insert
INSERT INTO [person] 
([Username], [name], [Password])
VALUES ( @Username_1, @Name_2, @Password_3)
GO