console.log("script loaded..");

$("body").on({
    click: (e)=> {
        console.log('clicked');
        console.log(e.pageX, e.pageY)
        console.log(e.which)
        console.log(e.target)
    },
    dblclick: (e)=> {
        console.log('double clicked');
    }

});


socket.on('connect', function() {
    console.log("connecting..")
    socket.emit('my_event', {data: 'I\'m connected!'
    });
});
