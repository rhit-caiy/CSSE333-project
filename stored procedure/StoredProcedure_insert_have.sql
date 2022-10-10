--add meal plan to the person in the database
--EXECUTE [add_mealpan_to_person] <Username> <MealPlanID>
USE [10_MealPlan]
GO
CREATE PROCEDURE [add_mealpan_to_person]
(@Username varchar(50),
@MealPlanID int)
AS
--if either username or meal plan ID is null
If (@Username is null or @MealPlanID is null)
Begin
	RAISERROR('User name or meal plan ID cannot be null', 14, 1);
	RETURN 1; 
End;

--Return an error code and print error message if the field doesn't exist
IF (NOT EXISTS (SELECT * FROM [person] WHERE Username = @Username) or not EXISTS (SELECT * FROM [MealPlan] WHERE [ID] = @MealPlanID))
BEGIN
	RAISERROR('Person username or meal plan ID does not exist in the table.', 14, 2);
	RETURN 2;
END;

--add meal plan to person
INSERT INTO [have] 
([Username], [MealPlanID])
VALUES (@Username, @MealPlanID)
GO
