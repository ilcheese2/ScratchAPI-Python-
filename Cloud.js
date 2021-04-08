var fs = require('fs');
var scratch = require('scratch-api');

function cloudVariable(projId, username, password, varName, varValue) {
  scratch.UserSession.create(username, password, function (err, user) { 
    user.cloudSession(Number(projId), function (err, cloud) {
      cloud.set(varName, varValue);
    });
  });
};

function setVar() {
  fs.readFile('communicate.txt', 'utf-8', function(err, data) {
    if (err) throw err;
    let info = data.replace(/^\./gim, 'myString').split('\n');
    let projId = info[0];
    let username = info[1];
    let password = info[2];
    let varName = info[3];
    let varValue = info[4];
    cloudVariable(projId, username, password, varName, varValue);
  });
};
setVar();
