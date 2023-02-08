/*What query would you run to get all the countries that speak Slovene?
 Your query should return the name of the country, language and language percentage.
 Your query should arrange the result by language percentage in descending order*/
select * from countries
join languages on countries.id =languages.country_id
where language like 'Slovene';
SELECT name,language,percentage from countries
JOIN languages ON countries.id = languages.country_id
WHERE language like 'Slovene'
ORDER BY percentage DESC;
/* What query would you run to display the total number of cities for each country? 
Your query should return the name of the country and the total number of cities.
 Your query should arrange the result by the number of cities in descending order*/
SELECT countries.name,count(country_id) as number_cities FROM countries
LEFT JOIN cities on countries.id=cities.country_id
GROUP BY countries.name
ORDER BY number_cities DESC;

/*What query would you run to get all the cities in Mexico with a population of greater than 500,000?
 Your query should arrange the result by population in descending order.*/
SELECT countries.name, cities.name, cities.population from countries
LEFT JOIN cities ON countries.id=cities.country_id
WHERE countries.name like 'Mexico' and cities.population > 500000
ORDER BY cities.population DESC;
/*What query would you run to get all languages in each country with a percentage greater than 89%? 
Your query should arrange the result by percentage in descending order.*/
select countries.name,languages.language,languages.percentage from countries
join languages on countries.id =languages.country_id
ORDER BY languages.percentage DESC;
/*What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000*/
SELECT countries.name,countries.surface_area,cities.population  FROM countries
LEFT JOIN cities on countries.id=cities.country_id
WHERE countries.surface_area < 501 and cities.population > 100000;
/* What query would you run to get countries with only Constitutional Monarchy countries
with a capital greater than 200 and a life expectancy greater than 75 years? */
SELECT name, government_form,capital, life_expectancy from countries
WHERE capital > 200
AND government_form ="Constitutional Monarchy"
AND life_expectancy > 75;
/*What query would you run to get all the cities of Argentina inside the Buenos Aires district 
and have the population greater than 500, 000? 
The query should return the Country Name, City Name, District and Population*/
SELECT countries.name,cities.name,cities.district,cities.population FROM countries
LEFT JOIN cities on countries.id=cities.country_id
WHERE countries.name like 'Argentina' and cities.district like 'Buenos Aires' and cities.population> 500000
ORDER BY cities.population DESC;
/*What query would you run to summarize the number of countries in each region? 
The query should display the name of the region and the number of countries. 
Also, the query should arrange the result by the number of countries in descending orde*/
SELECT countries.region, COUNT(countries.name) as countries_num
FROM countries
GROUP BY countries.region
ORDER BY countries_num DESC;