-- Drop the tables if they exist
DROP TABLE IF EXISTS StationService;
DROP TABLE IF EXISTS Beoordelingen;
DROP TABLE IF EXISTS Bericht;

-- Create a table for the geplaatste reviews
CREATE TABLE Bericht (
    BerichtID SERIAL NOT NULL,
    Bericht TEXT NOT NULL,
    _DateTime timestamp NOT NULL,
    ReizigerNaam VARCHAR(255) NOT NULL,
    Station VARCHAR(255) NOT NULL
);

-- Create a table for the beoordelingen
CREATE TABLE Beoordelingen (
    BeoordelingID SERIAL NOT NULL,
    _DateTime timestamp NOT NULL,
    ModeratorNaam VARCHAR(255) NOT NULL,
    ModeratorEmail VARCHAR(255) NOT NULL,
    _BerichtID INT NOT NULL,
    IsGoedgekeurd BOOLEAN NOT NULL
);

ALTER TABLE Bericht ADD PRIMARY KEY(BerichtID);
ALTER TABLE Beoordelingen ADD PRIMARY KEY(BeoordelingID);
ALTER TABLE Beoordelingen ADD FOREIGN KEY (_BerichtID) REFERENCES Bericht (BerichtID);

INSERT INTO Bericht (Bericht, _DateTime, ReizigerNaam, Station) VALUES ('MESSAGE', '2008-11-11 13:23:44', 'nameee', 'Station')

-- Create a table for StationService
CREATE TABLE StationService (
    station_city VARCHAR(50) PRIMARY KEY NOT NULL,
    country VARCHAR(2) NOT NULL,
    ov_bike BOOLEAN NOT NULL,
    elevator BOOLEAN NOT NULL,
    toilet BOOLEAN NOT NULL,
    park_and_ride BOOLEAN NOT NULL
);

INSERT INTO StationService (station_city, country, ov_bike, elevator, toilet, park_and_ride)
VALUES
('Arnhem', 'NL', true, false, true, false),
('Almere', 'NL', false, true, false, true),
('Amersfoort', 'NL', true, false, true, false),
('Almelo', 'NL', false, true, false, true),
('Alkmaar', 'NL', true, false, true, false),
('Apeldoorn', 'NL', false, true, false, true),
('Assen', 'NL', true, false, true, false),
('Amsterdam', 'NL', false, true, false, true),
('Boxtel', 'NL', true, false, true, false),
('Breda', 'NL', false, true, false, true),
('Dordrecht', 'NL', true, false, true, false),
('Delft', 'NL', false, true, false, true),
('Deventer', 'NL', true, false, true, false),
('Enschede', 'NL', false, true, false, true),
('Gouda', 'NL', true, false, true, false),
('Groningen', 'NL', false, true, false, true),
('Den Haag', 'NL', true, false, true, false),
('Hengelo', 'NL', false, true, false, true),
('Haarlem', 'NL', true, false, true, false),
('Helmond', 'NL', false, true, false, true),
('Hoorn', 'NL', true, false, true, false),
('Heerlen', 'NL', false, true, false, true),
('Den Bosch', 'NL', true, false, true, false),
('Hilversum', 'NL', false, true, false, true),
('Leiden', 'NL', true, false, true, false),
('Lelystad', 'NL', false, true, false, true),
('Leeuwarden', 'NL', true, false, true, false),
('Maastricht', 'NL', false, true, false, true),
('Nijmegen', 'NL', true, false, true, false),
('Oss', 'NL', false, true, false, true),
('Roermond', 'NL', true, false, true, false),
('Roosendaal', 'NL', false, true, false, true),
('Sittard', 'NL', true, false, true, false),
('Tilburg', 'NL', false, true, false, true),
('Utrecht', 'NL', true, false, true, false),
('Venlo', 'NL', false, true, false, true),
('Vlissingen', 'NL', true, false, true, false),
('Zaandam', 'NL', false, true, false, true),
('Zwolle', 'NL', true, false, true, false),
('Zutphen', 'NL', false, true, false, true);
