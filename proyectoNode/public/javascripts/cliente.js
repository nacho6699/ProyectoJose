// $(document).ready(function() {
// 	alert("Hola");
// });
var socket=io.connect("http://localhost:3000/");
socket.on('inicio_server',function(mensaje){
	$("#pagina").html(mensaje);
});

socket.on('mensaje_del_servidor',function(mensaje){
	
	$("#pagina").append('<li><img src="/media/imgUsuario/imagenx.jpg" width="50px">'+mensaje+'</li>');
	
});

$(function(){
	$("#enviar").click(function(event) {
		mensaje=$("#nombre").text()+" > "+$("#mensaje").val();
		socket.emit("mensaje_del_cliente",mensaje);
	});
});

