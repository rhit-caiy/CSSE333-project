USE [10_MealPlan]
GO

CREATE USER [caiy] FROM LOGIN [caiy]; 

exec sp_addrolemember 'db_owner', 'caiy'; 

GO

CREATE USER [jul] FROM LOGIN [jul]; 

exec sp_addrolemember 'db_owner', 'jul'; 

GO

CREATE USER [jiangy10] FROM LOGIN [jiangy10]; 

exec sp_addrolemember 'db_owner', 'jiangy10'; 

GO