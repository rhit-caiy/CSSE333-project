use [10__MealPlan]

go
insert into person select * from [10_MealPlan]..person
go
insert into food select * from [10_MealPlan]..food
go
insert into ingredient select * from [10_MealPlan]..ingredient
go
insert into	MealPlan select * from [10_MealPlan]..MealPlan
go
insert into isIngredientOf select * from [10_MealPlan]..isIngredientOf
go
insert into have select * from [10_MealPlan]..have
go
insert into [include] select * from [10_MealPlan]..[include]
go