var http = require('http');
var url = require('url');
var fs = require('fs');
var sign = "";
http.createServer(function (req, res) {
    console.log("Got Request for " + req.url);
    var q = url.parse(req.url, true);
    var qdata = q.query;
    if (q.pathname == "/connect") {
        res.writeHead(200, {'Content-Type': 'text/html'});
    }
    else if (q.pathname == "/getsign") {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(sign);
    }
    else if (q.pathname == "/%0Aconnect") {
        res.writeHead(200, {'Content-Type': 'text/html'});
    }
    else if (q.pathname == "/postsign") {
        if (qdata.text) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            sign = qdata.text
        }
        else {
            res.writeHead(400, {'Content-Type': 'text/html'});
        }
    }
    else {
        res.writeHead(404, {'Content-Type': 'text/html'});
    }
    res.end();
}).listen(1998);
console.log("Ready on port 1998");