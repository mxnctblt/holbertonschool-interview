#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    getCharacters(characters, 0);
  }
});

function getCharacters (url, index) {
  request(url[index], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < url.length) getCharacters(url, ++index);
    }
  });
}
