#!/usr/bin/node
//computes the number of tasks completed by user id.
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <url>');
  process.exit(1);
}
const url = process.argv[2];


// display request's status code
request.get(`${url}`, (err, res, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  const completed = {};
  const data = JSON.parse(body);

  data.forEach((task) => {
    if (task.completed) {
      if (!completed[task.userId]) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  });
  console.log(completed);
});
