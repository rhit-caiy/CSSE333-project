--insert prefer into database
--EXECUTE [insert_prefer] <Username> <ingredient name>
CREATE PROCEDURE [insert_Prefer]
(@Username varchar(50),
@ingredientname varchar(50))
AS
--if either name is null
if (@Username is null or @ingredientname is null)
begin
	RAISERROR('name cannot be null', 14, 1);
	RETURN 1; 
end;

--if name not exist for food or ingredient
if ((not EXISTS (SELECT * FROM [person] WHERE [Username] = @Username)) or (not EXISTS (SELECT * FROM [ingredient] WHERE [name] = @ingredientname)))
begin
	RAISERROR('not exist name', 14, 1);
	RETURN 2; 
end;

--insert
INSERT INTO [prefer] 
([Username],[IngredientName])
VALUES ( @Username, @ingredientname)
GO