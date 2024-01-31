#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./0-readme.js <file-path> <new_str>');
  process.exit(1);
}
const filePath = process.argv[2];
const new_str = process.argv[3];

fs.writeFile(filePath, new_str, err => {
  if (err) {
    console.error(err);
  }
});
