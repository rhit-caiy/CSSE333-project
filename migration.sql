create database [10__MealPlan]
GO
use [10__MealPlan]

CREATE USER [jiangy10] FOR LOGIN [jiangy10] WITH DEFAULT_SCHEMA=[dbo]
GO

CREATE USER [jul] FOR LOGIN [jul] WITH DEFAULT_SCHEMA=[dbo]
GO

CREATE USER [SodaBaseUsercaiy] FOR LOGIN [SodaBaseUsercaiy] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [jiangy10]
GO
ALTER ROLE [db_owner] ADD MEMBER [jul]
GO
ALTER ROLE [db_owner] ADD MEMBER [SodaBaseUsercaiy]
GO
/****** Object:  Table [dbo].[food]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[food](
	[name] [varchar](50) NOT NULL,
	[instruction] [varchar](max) NULL,
 CONSTRAINT [PK_food] PRIMARY KEY CLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[have]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[have](
	[Username] [varchar](50) NOT NULL,
	[MealPlanID] [int] NOT NULL,
	[Quantity] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Username] ASC,
	[MealPlanID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[include]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[include](
	[FoodName] [varchar](50) NOT NULL,
	[MealPlanID] [int] NOT NULL,
	[type] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[FoodName] ASC,
	[MealPlanID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ingredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ingredient](
	[name] [varchar](50) NOT NULL,
 CONSTRAINT [PK_ingredient] PRIMARY KEY CLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[isIngredientOf]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[isIngredientOf](
	[FoodName] [varchar](50) NOT NULL,
	[IngredientName] [varchar](50) NOT NULL,
	[quantity] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[FoodName] ASC,
	[IngredientName] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MealPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MealPlan](
	[ID] [int] NOT NULL,
	[date] [datetime] NOT NULL,
 CONSTRAINT [PK_MealPlan] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[person]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[person](
	[Username] [varchar](50) NOT NULL,
	[name] [varchar](50) NULL,
	[password] [varchar](max) NOT NULL,
 CONSTRAINT [PK_person] PRIMARY KEY CLUSTERED 
(
	[Username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[have]  WITH CHECK ADD  CONSTRAINT [FK__have__MealPlanID__3A81B327] FOREIGN KEY([MealPlanID])
REFERENCES [dbo].[MealPlan] ([ID])
GO
ALTER TABLE [dbo].[have] CHECK CONSTRAINT [FK__have__MealPlanID__3A81B327]
GO
ALTER TABLE [dbo].[have]  WITH CHECK ADD  CONSTRAINT [FK__have__Username__398D8EEE] FOREIGN KEY([Username])
REFERENCES [dbo].[person] ([Username])
GO
ALTER TABLE [dbo].[have] CHECK CONSTRAINT [FK__have__Username__398D8EEE]
GO
ALTER TABLE [dbo].[include]  WITH CHECK ADD FOREIGN KEY([FoodName])
REFERENCES [dbo].[food] ([name])
GO
ALTER TABLE [dbo].[include]  WITH CHECK ADD  CONSTRAINT [FK__include__MealPla__3E52440B] FOREIGN KEY([MealPlanID])
REFERENCES [dbo].[MealPlan] ([ID])
GO
ALTER TABLE [dbo].[include] CHECK CONSTRAINT [FK__include__MealPla__3E52440B]
GO
ALTER TABLE [dbo].[isIngredientOf]  WITH CHECK ADD FOREIGN KEY([FoodName])
REFERENCES [dbo].[food] ([name])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[isIngredientOf]  WITH CHECK ADD FOREIGN KEY([IngredientName])
REFERENCES [dbo].[ingredient] ([name])
GO
/****** Object:  StoredProcedure [dbo].[add_food_to_mealplan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[add_food_to_mealplan]
(@FoodName varchar(50),
@MealPlanID int,
@type varchar(10))
AS
--if any field is null
If (@FoodName is null or @MealPlanID is null)
Begin
	RAISERROR('Food name or meal plan ID cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the field doesn't exist
IF (NOT EXISTS (SELECT * FROM [food] WHERE name = @FoodName) or NOT EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @MealPlanID))
BEGIN
	RAISERROR('Person username or meal plan ID does not exist in the table.', 14, 2);
	RETURN 2;
END;


if (exists (select * from [include] where FoodName=@FoodName and MealPlanID=@MealPlanID))
begin
	raiserror('already exist food in meal plan',14,4);
	return 4;
end

--add food to meal plan
INSERT INTO [include] 
([FoodName],[MealPlanID],[type])
VALUES (@FoodName, @MealPlanID,@type)
GO
/****** Object:  StoredProcedure [dbo].[add_mealpan_to_person]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[add_mealpan_to_person]
(@Username varchar(50),
@MealPlanID int,
@Quantity int)
AS
--if either username or meal plan ID is null
If (@Username is null or @MealPlanID is null or @Quantity is null)
Begin
	RAISERROR('User name, meal plan ID or quantity cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the field doesn't exist
IF (NOT EXISTS (SELECT * FROM [person] WHERE Username = @Username) or not EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @MealPlanID))
BEGIN
	RAISERROR('Person username or meal plan ID does not exist in the table.', 14, 2);
	RETURN 2;
END;

IF (@Quantity = 0)
Begin
	Raiserror('Quantity of meal plan cannot be 0.', 14, 3);
	Return 3;
End

--add meal plan to person
INSERT INTO [have] 
([Username], [MealPlanID], [Quantity])
VALUES (@Username, @MealPlanID, @Quantity)
GO
/****** Object:  StoredProcedure [dbo].[addFoodToMealPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE proc [dbo].[addFoodToMealPlan](@username varchar(25), @food varchar(50), @type varchar(10))
as
begin
declare @planId int
select @planId = mealPlanId from have where username = @username

insert into include(MealPlanID, FoodName, type)
values(@planId, @food, @type)


end
GO
/****** Object:  StoredProcedure [dbo].[delete_food]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create proc [dbo].[delete_food](@foodName varchar(25))
as

begin
	if(not exists (select * from food where name = @foodName))
		begin
		raiserror('food not exist', 14,1);
		return 1;
		end
	delete from food where name = @foodName
end
GO
/****** Object:  StoredProcedure [dbo].[delete_food_ingredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE proc [dbo].[delete_food_ingredient](@foodName varchar(50))
as

begin
	delete from isIngredientOf where FoodName = @foodName
end
GO
/****** Object:  StoredProcedure [dbo].[delete_have]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[delete_have]
(@ID int)
AS
--if meal plan ID is null
if (@ID is null)
begin
	RAISERROR('Meal plan ID cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID doesn't exist
if ((NOT EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID)) and (NOT EXISTS (SELECT * FROM [have] WHERE [mealplanID] = @ID)))
begin
	RAISERROR('does not exist ID', 14, 2);
	RETURN 2; 
end;

--delete meal plan
DELETE [have] 
WHERE ([mealplanID] = @ID);
GO
/****** Object:  StoredProcedure [dbo].[delete_ingredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create proc [dbo].[delete_ingredient](@ingredientName varchar(25))
as
begin
	if(not exists (select * from ingredient where name = @ingredientName))
		begin
		raiserror('ingredient not exist', 14, 1);
		return 1;
		end
	delete from ingredient where name = @ingredientName
end
GO
/****** Object:  StoredProcedure [dbo].[delete_mealplan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[delete_mealplan]
(@ID int)
AS
--if meal plan ID is null
if (@ID is null)
begin
	RAISERROR('Meal plan ID cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID doesn't exist
if (NOT EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID))
begin
	RAISERROR('does not exist ID', 14, 2);
	RETURN 2; 
end;

--delete meal plan
DELETE [MealPlan] 
WHERE ([ID] = @ID);
GO
/****** Object:  StoredProcedure [dbo].[delete_person]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[delete_person]
(@Username varchar(50),
@name varchar(50),
@password varchar(MAX))
AS
--if username is null
if (@Username is null or @password is null)
begin
	RAISERROR('Username or password cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID or password doesn't exist
if (NOT EXISTS (Select [Username] From [Person] Where [Username] = @Username and Password = @password))
begin
	RAISERROR('does not exist Username or password', 14, 2);
	RETURN 2; 
end;

--delete meal plan
DELETE [person] 
WHERE ([Username] = @Username AND [name] = @name AND [password] = @password);
GO
/****** Object:  StoredProcedure [dbo].[deleteFoodOnPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE proc [dbo].[deleteFoodOnPlan](@username varchar(25),@id int, @food varchar(25))
as



delete 
from include
where MealPlanID = @id and foodName = @food
GO
/****** Object:  StoredProcedure [dbo].[edit_food]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

create proc [dbo].[edit_food](@foodName varchar(25), @newName varchar(25), @newInstruction varchar(100))
as

begin
	if(not exists (select * from food where name = @foodName))
		begin
		raiserror('food not exist', 14,1);
		return 1;
		end
	
	if(exists(select * from food where name = @newName))
		begin
		raiserror('food name already exist', 14, 2)
		return 2;
		end

	if(@newInstruction is not null)
		begin
		update food
		set instruction = @newInstruction
		where name = @foodName
		end

	if(@newName is not null)
		begin
		update food
		set name = @newname
		where name = @foodName
		end

end
GO
/****** Object:  StoredProcedure [dbo].[edit_ingredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create proc [dbo].[edit_ingredient](@ingredientName varchar(25), @newName varchar(25))
as
begin
	if(not exists (select * from ingredient where name = @ingredientName))
		begin
		raiserror('ingredient not exist', 14, 1);
		return 1;
		end
	if(exists (select * from ingredient where name = @newName))
		begin
		raiserror('ingredient name already exist', 14, 2);
		return 2;
	end
	update ingredient
	set name = @newName
	where name = @ingredientName
end
GO
/****** Object:  StoredProcedure [dbo].[editFoodOnPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE proc [dbo].[editFoodOnPlan](@id int, @food varchar(25), @changeTo varchar(25))
as
if (not exists (select * from food where food.name=@changeTo))
begin
	raiserror('food replaced should not be null',14,1);
	return 1;
end

update include
set foodName = @changeTo
where mealPlanId = @id and foodName = @food
GO
/****** Object:  StoredProcedure [dbo].[exist_Person]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[exist_Person]
(@Username varchar(50),
@Password varchar(MAX))
AS
Select * From Person where Username=@Username and Password=@Password
GO
/****** Object:  StoredProcedure [dbo].[get_allMealPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_allMealPlan]
AS
Select ID From MealPlan
GO
/****** Object:  StoredProcedure [dbo].[get_Food]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_Food]
AS
Select * From Food
GO
/****** Object:  StoredProcedure [dbo].[get_foodIngredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_foodIngredient]
(@foodname varchar(50))
AS
Select * From food
join isIngredientOf on food.name=isIngredientOf.FoodName
join ingredient on ingredient.name=isIngredientOf.IngredientName
where food.name=@foodname
GO
/****** Object:  StoredProcedure [dbo].[get_Ingredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_Ingredient]
AS
Select * From Ingredient
GO
/****** Object:  StoredProcedure [dbo].[get_MealPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_MealPlan]
(@Username varchar(50))
AS

Select max(MealPlan.date) as date,count(include.FoodName) as quantity
from MealPlan--Quantity From MealPlan
join have on have.MealPlanID=MealPlan.ID
left join [include] on [include].MealPlanID=MealPlan.ID
group by have.MealPlanID
having max(have.Username)=@Username
GO
/****** Object:  StoredProcedure [dbo].[get_personFood]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_personFood]
(@Username varchar(50))
AS
Select * From have
join include on have.MealPlanID=include.MealPlanID
join MealPlan on MealPlan.ID=have.MealPlanID
where have.Username=@Username
GO
/****** Object:  StoredProcedure [dbo].[get_personMealFood]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_personMealFood]
(@Username varchar(50),
@mealplanID int)
AS
Select * From have
join include on have.MealPlanID=include.MealPlanID
join MealPlan on MealPlan.ID=have.MealPlanID
where have.Username=@Username and MealPlan.ID=@mealplanID
GO
/****** Object:  StoredProcedure [dbo].[get_personMealplanID]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[get_personMealplanID]
(@Username varchar(50))
AS
Select ID From MealPlan
join have on have.MealPlanID=MealPlan.ID
where have.Username=@Username
GO
/****** Object:  StoredProcedure [dbo].[getFoodNotOnPlan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create proc [dbo].[getFoodNotOnPlan]
as
begin
select * from food full join include on food.name = include.foodName
where mealPlanId is null
end
GO
/****** Object:  StoredProcedure [dbo].[getIngredientNotInFood]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create proc [dbo].[getIngredientNotInFood]
as
begin
	select * from ingredient full join isIngredientOf on ingredient.name = isIngredientOf.IngredientName
	where foodName is null
end
GO
/****** Object:  StoredProcedure [dbo].[insert_Food]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--insert a food into database
--EXECUTE [insert_Food] <food name>
CREATE PROCEDURE [dbo].[insert_Food]
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
/****** Object:  StoredProcedure [dbo].[insert_Ingredient]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--insert an ingredient into database
--EXECUTE [insert_Ingredient] <ingredient name>
CREATE PROCEDURE [dbo].[insert_Ingredient]
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
/****** Object:  StoredProcedure [dbo].[insert_IsIngredientOf]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--insert isIngredientOf into database
--it should be executed immediately after create food and can not execute any more
--EXECUTE [insert_IsIngredientOf] <food name> <ingredient name> <quantity>
CREATE PROCEDURE [dbo].[insert_IsIngredientOf]
(@foodname varchar(50),
@ingredientname varchar(50),
@quantity int = 1)
AS
--if either name is null
if (@foodname is null or @ingredientname is null)
begin
	RAISERROR('name cannot be null', 14, 1);
	RETURN 1; 
end;

--if name not exist for food or ingredient
if ((not EXISTS (SELECT * FROM [food] WHERE [name] = @foodname)) or (not EXISTS (SELECT * FROM [ingredient] WHERE [name] = @ingredientname)))
begin
	RAISERROR('not exist name', 14, 1);
	RETURN 2; 
end;

--insert
INSERT INTO [isIngredientOf] 
([FoodName],[IngredientName],[quantity])
VALUES ( @foodname, @ingredientname, @quantity)
GO
/****** Object:  StoredProcedure [dbo].[insert_mealplan]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[insert_mealplan]
(@ID int,
@date datetime)
AS
--if fields are null
if (@ID is null)
begin
	RAISERROR('ID cannot be null', 14, 1);
	RETURN 1; 
end;

--if ID already exist
if (EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @ID))
begin
	RAISERROR('already exist ID', 14, 2);
	RETURN 2; 
end;

--insert the meal plan
INSERT INTO [MealPlan] 
([ID],[date])
VALUES ( @ID, @date)
GO
/****** Object:  StoredProcedure [dbo].[insert_Person]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[insert_Person]
(@Username_1 varchar(50),
@Name_2 varchar(50)=null,
@Password_3 varchar(MAX))
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
/****** Object:  StoredProcedure [dbo].[insert_Prefer]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--insert isIngredientOf into database
--it should be executed immediately after create food and can not execute any more
--EXECUTE [insert_IsIngredientOf] <food name> <ingredient name> <quantity>
CREATE PROCEDURE [dbo].[insert_Prefer]
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
/****** Object:  StoredProcedure [dbo].[update_name]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[update_name]
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
/****** Object:  StoredProcedure [dbo].[update_password]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[update_password]
(@Username varchar(50),
@oldPassword varchar(MAX),
@newPassword varchar(MAX))
AS
--if either name or password is null
If (@Username is null or @newPassword is null)
Begin
	RAISERROR('User name or password cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the person doesn't exist
IF (NOT EXISTS (SELECT * FROM [person] WHERE Username = @Username and Password = @oldPassword))
BEGIN
	RAISERROR('Person username does not exist or password incorrect in the table.', 14, 2);
	RETURN 2;
END;

--update person password
Update [person]
Set [password] = @newPassword
Where Username = @Username
GO
/****** Object:  StoredProcedure [dbo].[update_prefer]    Script Date: 11/7/2022 2:33:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[update_prefer]
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

--Return an error code and print error message if the ingredient doesn't exist
IF (NOT EXISTS (SELECT * From ingredient WHERE [name] = @newIngredientName))
BEGIN
	RAISERROR('This ingredient does not exist in the table.', 14, 3);
	RETURN 2;
END;

--update person preference
Update [prefer]
Set IngredientName = @newIngredientName
Where Username = @Username
GO
