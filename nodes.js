var mysql = require('mysql');


var con = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"bmvb"
});

con.connect(function (err){
if (err) {
  console.log("connected");
  return;
}
 else{
    console.log("fail");
 }

 con.query("CREATE DATABASE checks ", function (err, result) {
    if (err) throw err;
    console.log("Database created");
  });

});

