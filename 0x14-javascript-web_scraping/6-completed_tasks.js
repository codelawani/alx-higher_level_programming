#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed === true) {
        if (completed[tasks[i].userId]) {
          completed[tasks[i].userId] += 1;
        } else {
          completed[tasks[i].userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
