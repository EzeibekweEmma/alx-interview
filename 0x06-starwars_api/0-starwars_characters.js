#!/usr/bin/node
/**
 * 0x0F. Star Wars API
 */
const process = require("process");
const request = require("request");

if (process.argv.length !== 3) {
    process.exit(0);
}

function requestCharacter(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            error ? reject(error.message) : resolve(JSON.parse(body));
        });
    });
}

function requestApi() {
    const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
    request(url, async (error, response, body) => {
        error && new Error(error.message);
        const { characters } = JSON.parse(body);
        for (const index in characters) {
            await requestCharacter(characters[index])
                .then((res) => console.log(res.name))
                .catch((err) => console.log(err.message));
        }
    });
}

requestApi();
