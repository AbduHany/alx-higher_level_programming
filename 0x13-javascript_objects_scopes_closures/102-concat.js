#!/usr/bin/node
if (process.argv.length === 5) {
  const fs = require('fs');
  const writeData = function (data) {
    fs.writeFileSync(process.argv[4], data, (err) => {
      if (err) { throw err; }
    });
  };
  const str1 = fs.readFileSync(process.argv[2], 'utf8', (err) => {
    if (err) { throw err; }
  });
  const str2 = fs.readFileSync(process.argv[3], 'utf8', (err) => {
    if (err) { throw err; }
  });
  writeData(str1 + str2);
}
