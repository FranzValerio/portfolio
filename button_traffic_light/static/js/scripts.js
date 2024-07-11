var socket = io();
var username = '';

function join() {
    username = document.getElementById('username').value;
    if (username) {
        socket.emit('join', { username: username });
        document.getElementById('login').style.display = 'none';
        document.getElementById('controls').style.display = 'block';
    }
}

function changeStatus(status) {
    socket.emit('status_change', { username: username, status: status });
}

socket.on('update_status', function(data) {
    var statusList = document.getElementById('status_list');
    statusList.innerHTML = '';
    for (var user in data) {
        var color = data[user] === 'green' ? 'green' : 'red';
        statusList.innerHTML += '<p>' + user + ': <span style="color:' + color + ';">' + data[user] + '</span></p>';
    }
});
