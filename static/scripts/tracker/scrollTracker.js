console.log("Scroll tracker");
socket.on('connect', function() {
    console.log("connecting..")
    socket.emit('my_event', {data: 'I\'m connected!'
    });
});