var io=require('socket.io');
exports.initialize=function(server){
	io=io.listen(server);
	io.sockets.on("connection",function(socket){
		mensaje="Chat General";
		socket.emit('inicio_server',mensaje);

		socket.on("mensaje_del_cliente",function(datos){
			msj=datos;
			io.sockets.emit("mensaje_del_servidor",msj);
		});
	});
}
