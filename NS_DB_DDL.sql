-- Maak een nieuwe database met de naam 'reviewwebsite'
CREATE DATABASE reviewwebsite;

-- Gebruik de gemaakte database
USE reviewwebsite;

-- Maak een tabel voor de geplaatste reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    Bericht TEXT,
    DatumTijdBericht DATETIME,
    ReizigerNaam VARCHAR(255),
    Station VARCHAR(255),
);

-- Maak een tabel voor de beoordelingen
CREATE TABLE Beoordelingen (
    BeoordelingID INT AUTO_INCREMENT PRIMARY KEY,
    DatumTijdBeoordeling DATETIME,
    ModeratorNaam VARCHAR(255),
    ModeratorEmail VARCHAR(255),
    FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID),
    IsGoedgekeurd BOOLEAN
);
