USE master
GO
IF NOT EXISTS (
 SELECT name
 FROM sys.databases
 WHERE name = N'nba_db'
)
 CREATE DATABASE [nba_db];
GO
IF SERVERPROPERTY('ProductVersion') > '12'
 ALTER DATABASE [nba_db] SET QUERY_STORE=ON;
GO