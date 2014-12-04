var express= require('express');
var http=require('http');
var port=3000;
var path=require('path');


var app=express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.engine('jade', require('jade').__express);
app.use(express.static(__dirname + '/public'));


app.get("/",function(req, res){
	res.render("index");
});

var server=http.createServer(app).listen(port,function(){
	console.log("Servidor iniciado en el puerto "+ port);
});
require('./routes/sockets.js').initialize(server);