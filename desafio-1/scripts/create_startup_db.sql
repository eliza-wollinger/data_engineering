USE master
GO
IF NOT EXISTS (
 SELECT name
 FROM sys.databases
 WHERE name = N'startup_db'
)
 CREATE DATABASE [startup_db];
GO
IF SERVERPROPERTY('ProductVersion') > '12'
 ALTER DATABASE [startup_db] SET QUERY_STORE=ON;
GO