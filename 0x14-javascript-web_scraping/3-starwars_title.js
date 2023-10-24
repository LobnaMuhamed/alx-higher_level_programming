#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request.get(url, (error, response, body) => {
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(`${movie.title}`);
  } else if (error) { console.log(error); } else { console.log(`Error code: ${response.statusCode}`); }
});
