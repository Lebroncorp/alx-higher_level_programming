#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./0-readme.js <file-path> <newstr>');
  process.exit(1);
}
const filePath = process.argv[2];
const newstr = process.argv[3];

fs.writeFile(filePath, newstr, err => {
  if (err) {
    console.error(err);
  }
});
