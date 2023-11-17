--  lists all the cities of California that can be found
-- in ascending order of the cities.id
SELECT id,name FROM cities
where state_id =(
	SELECT id FROM states
	WHERE name = 'California'
);
