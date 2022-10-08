--insert a food into database
--EXECUTE [insert_Food] <food name>
CREATE PROCEDURE [insert_Food]
(@name varchar(50),
@instruction varchar(max) = null)
AS
--if name is null
if (@name is null)
begin
	RAISERROR('food name cannot be null', 14, 1);
	RETURN 1; 
end;

--if name already exist
if (EXISTS (SELECT * FROM [food] WHERE [name] = @name))
begin
	RAISERROR('already exist name', 14, 1);
	RETURN 2; 
end;

--insert
INSERT INTO [food] 
([name],[instruction])
VALUES ( @name, @instruction)
GO