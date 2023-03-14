#!/usr/bin/node
const fs = require('fs');
const [srcfile1, srcfile2, destfile] = process.argv.slice(2);
const filecontent1 = fs.readFileSync(srcfile1, 'utf-8');
const filecontent2 = fs.readFileSync(srcfile2, 'utf-8');
const newContent = filecontent1 + filecontent2;
fs.writeFileSync(destfile, newContent);
