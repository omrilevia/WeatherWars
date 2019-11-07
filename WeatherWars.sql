

use master
GO
if exists (select * from master.sys.databases where name = 'WeatherWars')
  drop database WeatherWars
GO
create database WeatherWars
GO
use WeatherWars
GO

CREATE TABLE player (
  userName varchar(25) not null,
  password      varchar(40) not null,
  dob       date not null, 
  email varchar(50),
  phoneNumber varchar(10),
  primary key (userName)
);

CREATE TABLE history (
  userName varchar(25) not null,
  earnings decimal(7,2),
  currentStreak integer check (currentStreak >= 0),
  maxStreak integer check (maxStreak >= 0),
  gamesWon integer check (gamesWon >= 0),
  totalGames integer check (totalGames >= 0),
  foreign key(userName) references player(userName) 
	on delete cascade on update cascade
);

CREATE TABLE team (
  tId integer IDENTITY(0,1) not null,
  teamName varchar(50),
  primary key(tId) 
);

CREATE TABLE contest (
  cId integer IDENTITY(0,1) not null,
  weatherType varchar(25) not null check (weatherType in ('Heat', 'Cold', 'Wind', 'Rain')),
  duration varchar(25) not null check (duration in ('Daily', 'Weekly', 'Seasonal')),
  scoringType varchar(25) not null check (scoringType in ('Extremes', 'Predictions')),
  rotatingType varchar(25) default('classic'),
  timeCreated datetime not null,
  status varchar(25) not null check (status in ('Pending', 'Running', 'Finished')),
  primary key(cId)
);

CREATE TABLE cities (
	cName varchar(25) not null,
	geoId varchar(25) not null,
	cState varchar(25) not null,
	primary key(cName)
);

CREATE TABLE weather (
  cName varchar(25) not null,
  lastUpdated datetime not null,
  currentDate date not null,
  tHigh float not null,
  tLow float not null,
  rainLevel float not null,
  windSpeed float not null
  primary key(cName, currentDate),
  foreign key(cName) references cities(cName) on delete cascade
	on update cascade
);

CREATE TABLE refers (
	referrer varchar(25) not null,
	referee varchar(25) not null,
	primary key(referrer, referee),
	foreign key(referrer) references player(userName),
	foreign key(referee) references player(userName)
);

CREATE TABLE buyInto (
	userName varchar(25) not null,
	cId integer not null,
	tId integer not null,
	primary key(userName, cId, tId),
	foreign key (userName) references player(userName) on delete cascade on update cascade,
	foreign key (cId) references contest(cId) on delete cascade on update cascade,
	foreign key (tId) references team(tId) on delete cascade on update cascade
);

CREATE TABLE comprisedOf (
	tId integer not null,
	cName varchar(25) not null,
	prediction integer,
	primary key (tId, cName),
	foreign key(tId) references team(tId) on delete cascade on update cascade,
	foreign key (cName) references cities(cName) on delete cascade on update cascade
);

CREATE TABLE paymentInfo (
	userName varchar(25) not null,
	cardNumber char(16) not null,
	primary key(userName),
	foreign key(userName) references player (userName) on update cascade on delete cascade
);


	


