var http = require('http');
http.createServer(function(req, res){
    res.writeHead(200,{"Content-Type": "text/plain"});
    res.end('Hello Word\n');
}).listen(8081);

console.log('Sever dang chay tai http://127.0.0.1:8081/');