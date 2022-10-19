--add meal plan to the person in the database
--EXECUTE [add_mealpan_to_person] <Username> <MealPlanID>
USE [10_MealPlan]
GO
Create PROCEDURE [add_mealpan_to_person]
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
