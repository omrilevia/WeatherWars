

drop database if exists WeatherWars;
create database WeatherWars;
use WeatherWars;

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
  earnings float,
  currentStreak integer check (currentStreak >= 0),
  maxStreak integer check (maxStreak >= 0),
  gamesWon integer check (gamesWon >= 0),
  totalGames integer check (totalGames >= 0),
  foreign key(userName) references player(userName) 
	on delete cascade on update cascade
);

CREATE TABLE team (
  tId integer AUTO_INCREMENT not null,
  teamName varchar(50),
  primary key(tId) 
);

CREATE TABLE contest (
  cId integer AUTO_INCREMENT not null,
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
  windSpeed float not null,
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


/* view to show pending and running contests */



/* all running contests and their players' scores for extremes */
use WeatherWars;
create view runningContestScoresExtremesDaily
as select b.cId as 'contest#', userName, sum(tHigh) as 'HeatScore', sum(tLow) as 'ColdScore', sum(rainLevel) as 'RainScore', sum(windSpeed) as 'WindScore'		
from buyInto as b join contest as c 
on b.cId = c.cId 
join team as t
on b.tId = t.tId
join comprisedOf on t.tId = comprisedOf.tId
join weather 
on comprisedOf.cName = weather.cName
where c.status = 'Running' and c.scoringType = 'Extremes' 
and month(weather.lastUpdated) = month((select DATE_ADD(c.timeCreated, interval 1 day)))
and day(weather.lastUpdated) = day((select DATE_ADD(c.timeCreated, interval 1 day)))
and year(weather.lastUpdated) = year((select DATE_ADD(c.timeCreated, interval 1 day)))
group by b.cId, userName;

create view runningContestScoresExtremesWeekly
as select b.cId as 'contest#', userName, sum(tHigh) as 'HeatScore', sum(tLow) as 'ColdScore', sum(rainLevel) as 'RainScore', sum(windSpeed) as 'WindScore'		/* show player totals */
from buyInto as b join contest as c 
on b.cId = c.cId 
join team as t
on b.tId = t.tId
join comprisedOf on t.tId = comprisedOf.tId
join weather 
on comprisedOf.cName = weather.cName
where c.status = 'Running' and c.scoringType = 'Extremes' 
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 3 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 10 day)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 3 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 10 day)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 3 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 10 day)))
group by b.cId, userName;

create view runningContestScoresExtremesSeasonal
as select b.cId as 'contest#', userName, sum(tHigh) as 'HeatScore', sum(tLow) as 'ColdScore', sum(rainLevel) as 'RainScore', sum(windSpeed) as WindScore		/* show player totals */
from buyInto as b join contest as c 
on b.cId = c.cId 
join team as t
on b.tId = t.tId
join comprisedOf on t.tId = comprisedOf.tId
join weather 
on comprisedOf.cName = weather.cName
where c.status = 'Running' and c.scoringType = 'Extremes' 
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 7 day))) and month(weather.lastUpdated) <= month((DATE_ADD(c.timeCreated, interval 3 month)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 7 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 3 month)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 7 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 3 month)))
group by b.cId, userName;

create view runningContestScoresPredictionsDaily
as select b.cId, userName, sum(abs(prediction - tHigh)) as 'HeatScore', sum(abs(prediction - tLow)) as 'ColdScore',
sum(abs(prediction - rainLevel)) as 'RainScore', sum(abs(prediction - windSpeed)) as 'WindScore'						/* show score based on prediction */
from buyInto as b join contest as c on b.cId = c.cId
join team as t on b.tId = t.tId
join comprisedOf as cO on t.tId = cO.tId
join weather on cO.cName = weather.cName
where c.status = 'Running' and c.scoringType = 'Predictions'
and month(weather.lastUpdated) = month((select DATE_ADD(c.timeCreated, interval 1 day)))
and day(weather.lastUpdated) = day((select DATE_ADD(c.timeCreated, interval 1 day)))
and year(weather.lastUpdated) = year((select DATE_ADD(c.timeCreated, interval 1 day)))
group by b.cId, userName;

create view runningContestScoresPredictionsWeekly
as select b.cId, userName, sum(abs(prediction - tHigh)) as 'HeatScore', sum(abs(prediction - tLow)) as 'ColdScore',
sum(abs(prediction - rainLevel)) as 'RainScore', sum(abs(prediction - windSpeed)) as 'WindScore'						/* show score based on prediction */
from buyInto as b join contest as c on b.cId = c.cId
join team as t on b.tId = t.tId
join comprisedOf as cO on t.tId = cO.tId
join weather on cO.cName = weather.cName
where c.status = 'Running' and c.scoringType = 'Predictions'
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 3 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 10 day)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 3 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 10 day)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 3 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 10 day)))
group by b.cId, userName;


create view runningContestScoresPredictionsSeasonal
as select b.cId, userName, sum(abs(prediction - tHigh)) as 'HeatScore', sum(abs(prediction - tLow)) as 'ColdScore',
sum(abs(prediction - rainLevel)) as 'RainScore', sum(abs(prediction - windSpeed)) as 'WindScore'						/* show score based on prediction */
from buyInto as b join contest as c on b.cId = c.cId
join team as t on b.tId = t.tId
join comprisedOf as cO on t.tId = cO.tId
join weather on cO.cName = weather.cName
where c.status = 'Running' and c.scoringType = 'Predictions'
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 7 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 3 month)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 7 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 3 month)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 7 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 3 month)))
group by b.cId, userName;


create view finishedContestScoresExtremesDaily
as select b.cId as 'contest#', userName, sum(tHigh) as 'HeatScore', sum(tLow) as 'ColdScore', sum(rainLevel) as 'RainScore', sum(windSpeed) as 'WindScore'		/* show player totals */
from buyInto as b join contest as c 
on b.cId = c.cId 
join team as t
on b.tId = t.tId
join comprisedOf on t.tId = comprisedOf.tId
join weather 
on comprisedOf.cName = weather.cName
where c.status = 'Finished' and c.scoringType = 'Extremes' 
and month(weather.lastUpdated) = month((select DATE_ADD(c.timeCreated, interval 1 day)))
and day(weather.lastUpdated) = day((select DATE_ADD(c.timeCreated, interval 1 day)))
and year(weather.lastUpdated) = year((select DATE_ADD(c.timeCreated, interval 1 day)))
group by b.cId, userName;


create view finishedContestScoresExtremesWeekly
as select b.cId as 'contest#', userName, sum(tHigh) as 'HeatScore', sum(tLow) as 'ColdScore', sum(rainLevel) as 'RainScore', sum(windSpeed) as 'WindScore'		/* show player totals */
from buyInto as b join contest as c 
on b.cId = c.cId 
join team as t
on b.tId = t.tId
join comprisedOf on t.tId = comprisedOf.tId
join weather 
on comprisedOf.cName = weather.cName
where c.status = 'Finished' and c.scoringType = 'Extremes' 
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 3 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 10 day)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 10 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 10 day)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 10 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 10 day)))
group by b.cId, userName;


create view finishedContestScoresExtremesSeasonal
as select b.cId as 'contest#', userName, sum(tHigh) as 'HeatScore', sum(tLow) as 'ColdScore', sum(rainLevel) as 'RainScore', sum(windSpeed) as 'WindScore'		/* show player totals */
from buyInto as b join contest as c 
on b.cId = c.cId 
join team as t
on b.tId = t.tId
join comprisedOf on t.tId = comprisedOf.tId
join weather 
on comprisedOf.cName = weather.cName
where c.status = 'Finished' and c.scoringType = 'Extremes' 
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 7 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 3 month)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 7 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 3 month)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 7 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 3 month)))
group by b.cId, userName;


create view finishedContestScoresPredictionsDaily
as select b.cId, userName, sum(abs(prediction - tHigh)) as 'HeatScore', sum(abs(prediction - tLow)) as 'ColdScore',
sum(abs(prediction - rainLevel)) as 'RainScore', sum(abs(prediction - windSpeed)) as 'WindScore'						/* show score based on prediction */
from buyInto as b join contest as c on b.cId = c.cId
join team as t on b.tId = t.tId
join comprisedOf as cO on t.tId = cO.tId
join weather on cO.cName = weather.cName
where c.status = 'Finished' and c.scoringType = 'Predictions'
and month(weather.lastUpdated) = month((select DATE_ADD(c.timeCreated, interval 1 day)))
and day(weather.lastUpdated) = day((select DATE_ADD(c.timeCreated, interval 1 day)))
and year(weather.lastUpdated) = year((select DATE_ADD(c.timeCreated, interval 1 day)))
group by b.cId, userName;

use WeatherWars;
create view finishedContestScoresPredictionsWeekly
as select b.cId, userName, sum(abs(prediction - tHigh)) as 'HeatScore', sum(abs(prediction - tLow)) as 'ColdScore',
sum(abs(prediction - rainLevel)) as 'RainScore', sum(abs(prediction - windSpeed)) as 'WindScore'						/* show score based on prediction */
from buyInto as b join contest as c on b.cId = c.cId
join team as t on b.tId = t.tId
join comprisedOf as cO on t.tId = cO.tId
join weather on cO.cName = weather.cName
where c.status = 'Finished' and c.scoringType = 'Predictions'
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 3 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 10 day)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 3 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 10 day)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 3 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 10 day)))
group by b.cId, userName;



create view finishedContestScoresPredictionsSeasonal
as select b.cId, userName, sum(abs(prediction - tHigh)) as 'HeatScore', sum(abs(prediction - tLow)) as 'ColdScore',
sum(abs(prediction - rainLevel)) as 'RainScore', sum(abs(prediction - windSpeed)) as 'WindScore'						/* show score based on prediction */
from buyInto as b join contest as c on b.cId = c.cId
join team as t on b.tId = t.tId
join comprisedOf as cO on t.tId = cO.tId
join weather on cO.cName = weather.cName
where c.status = 'Finished' and c.scoringType = 'Predictions'
and month(weather.lastUpdated) >= month((select DATE_ADD(c.timeCreated, interval 7 day))) and month(weather.lastUpdated) <= month((select DATE_ADD(c.timeCreated, interval 3 month)))
and day(weather.lastUpdated) >= day((select DATE_ADD(c.timeCreated, interval 7 day))) and day(weather.lastUpdated) <= day((select DATE_ADD(c.timeCreated, interval 3 month)))
and year(weather.lastUpdated) >= year((select DATE_ADD(c.timeCreated, interval 7 day))) and year(weather.lastUpdated) <= year((select DATE_ADD(c.timeCreated, interval 3 month)))
group by b.cId, userName;


