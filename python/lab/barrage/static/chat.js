$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};

    $("#messageform").on("submit", function() {
        newMessage($(this));
        return false;
    });
    $("#messageform").on("keypress", function(e) {
        if (e.keyCode == 13) {
            newMessage($(this));
            return false;
        }
    });
    $("#message").select();
    updater.start();
});

function newMessage(form) {
    var message = form.formToDict();
    updater.socket.send(JSON.stringify(message));
    form.find("input[type=text]").val("").select();
}

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

var updater = {
    socket: null,

    start: function() {
        var url = "ws://" + location.host + "/chatsocket";
        updater.socket = new WebSocket(url);
        updater.socket.onmessage = function(event) {
            updater.showMessage(JSON.parse(event.data));
        }
    },

    showMessage: function(message) {
        var existing = $("#m" + message.id);
        if (existing.length > 0) return;
        var node = $(message.html);
        node.hide();
        var n = node[0];
        var x = document.documentElement.clientWidth;
        var y = document.documentElement.clientHeight;

        n.style.position = "fixed"
        n.style.width = "500px"
        n.style.top = Math.floor(Math.random() * (y-100) + 25) + 'px'
        var left = Math.floor(Math.random() * x/8 + 7*x/8)
        var step = 5 + 5 * (.5 - Math.random())
        var time = Math.floor(15 + 10 * Math.random())
        n.style.left = x + 'px'
        n.style['-webkit-transition'] = 'all ' + time + 's ease-in-out'
        setTimeout(function(){    
            n.style['-webkit-transform'] = 'translate(-' + (x + 500)+ 'px, 0)'
            setTimeout(function(){    
                n.remove();
            }, time*1000)
        }, 5);
 
        $("#inbox").append(node);
        node.slideDown();
    }
};
