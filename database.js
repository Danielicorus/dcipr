var mysql = require('mysql');


var con = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"bmvb",
    database:"checks"
});


con.connect(function (err){
        if (err){
        console.log("Connected!");
        }
     con.query("CREATE TABLE show ( id integer PRIMARY KEY, name char(20) , phone integer )", function (err, result) {
        if (err) {
        console.log("table created");
        }
      });
    
    });
    





// con.connect(function (err){
//     if (err){
//     console.log("Connected!");
//     }
//  con.query("CREATE DATABASE checks ", function (err, result) {
//     if (err) {
//     console.log("Database created");
//     }
//   });

// });

