create database [10_MealPlan]
ON
PRIMARY (NAME=Data,    FILENAME='D:\Database\MSSQL15.MSSQLSERVER\MSSQL\DATA\Sample.mdf',   SIZE=6MB,
  MAXSIZE=30MB,
  FILEGROWTH=12%) 

LOG ON   (NAME=Log,   FILENAME= 'D:\Database\MSSQL15.MSSQLSERVER\MSSQL\DATA\Sample.ldf',   SIZE=3MB,
  MAXSIZE=22MB,
  FILEGROWTH=17%)

CREATE USER [caiy] FROM LOGIN [caiy]; 
exec sp_addrolemember 'db_owner', 'caiy'; 
GO

CREATE USER [jul] FROM LOGIN [jul]; 
exec sp_addrolemember 'db_owner', 'jul'; 
GO

CREATE USER [jiangy10] FROM LOGIN [jiangy10]; 
exec sp_addrolemember 'db_owner', 'jiangy10'; 
GO

create table person(
	Username varchar(50) primary key not null,
	[Name] varchar(50),
	[Password] varchar(MAX) not null
);

create table MealPlan(
	id int primary key not null,
	[date] datetime,
	[type] varchar(50)
);

create table food(
	[name] varchar(50) primary key not null,
	[instruction] varchar(MAX)
);

create table ingredient(
	[name] varchar(50) primary key not null
);

create table isIngredientOf(
	FoodName varchar(50) not null,
	IngredientName varchar(50) not null,
	quantity int,
	primary key (FoodName,IngredientName),
	foreign key (FoodName) references food(name),
	foreign key (IngredientName) references ingredient(name)
);

create table prefer(
	Username varchar(50) not null,
	IngredientName varchar(50) not null,
	primary key (Username,IngredientName),
	foreign key (Username) references person(Username),
	foreign key (IngredientName) references ingredient(name)
);

create table have(
	Username varchar(50) not null,
	MealPlanID int not null,
	primary key (Username,MealPlanID),
	foreign key (Username) references person(Username),
	foreign key (MealPlanID) references MealPlan(ID)
);

create table [include](
	FoodName varchar(50) not null,
	MealPlanID int not null,
	amount int,
	primary key (FoodName,MealPlanID),
	foreign key (FoodName) references Food(name),
	foreign key (MealPlanID) references MealPlan(ID)
);

create table PersonAllergy(
	Username varchar(50) not null,
	Allergy varchar(50) not null,
	primary key (Username,Allergy),
	foreign key (Username) references person(Username)
);

create table IngredientAllergy(
	IngredientName varchar(50) not null,
	Allergy varchar(50) not null,
	primary key (IngredientName,Allergy),
	foreign key (IngredientName) references ingredient(name)
);