# Project NS-Stations zuil Lucas Baneke
import DatabaseManager

DatabaseManager.ConnectToDB()

queries = [
    "DROP TABLE IF EXISTS StationService;",
    "DROP TABLE IF EXISTS Beoordelingen;",
    "DROP TABLE IF EXISTS Bericht;",
    "CREATE TABLE Bericht (BerichtID SERIAL NOT NULL, Bericht TEXT NOT NULL, _DateTime timestamp NOT NULL, ReizigerNaam VARCHAR(255) NOT NULL, Station VARCHAR(255) NOT NULL);",
    "CREATE TABLE Beoordelingen (BeoordelingID SERIAL NOT NULL, _DateTime timestamp NOT NULL, ModeratorNaam VARCHAR(255) NOT NULL, ModeratorEmail VARCHAR(255) NOT NULL, _BerichtID INT NOT NULL, IsGoedgekeurd BOOLEAN NOT NULL);",
    "ALTER TABLE Bericht ADD PRIMARY KEY (BerichtID);",
    "ALTER TABLE Beoordelingen ADD PRIMARY KEY (BeoordelingID);",
    "ALTER TABLE Beoordelingen ADD FOREIGN KEY (_BerichtID) REFERENCES Bericht (BerichtID);",
    "CREATE TABLE StationService (station_city VARCHAR(50) PRIMARY KEY NOT NULL, country VARCHAR(2) NOT NULL, ov_bike BOOLEAN NOT NULL, elevator BOOLEAN NOT NULL, toilet BOOLEAN NOT NULL, park_and_ride BOOLEAN NOT NULL);"
]

for query in queries:
    DatabaseManager.ExecuteSQL_Query(query, False, False)


import UserWindow
import Moderator
