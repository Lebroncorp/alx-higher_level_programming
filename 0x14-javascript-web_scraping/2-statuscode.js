#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  console.log('code:', res.statusCode);
});
