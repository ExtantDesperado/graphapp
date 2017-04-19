var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

function drawGraph(points) {
    context.strokeStyle = "black";
    var c = canvas.width/10;
    context.beginPath();
    context.moveTo(0,canvas.height/2-points[0]*c);
    for (var i = 1; i < points.length; i++) {
        context.lineTo(i*c/100,canvas.height/2-points[i]*c);
    }
    context.stroke();
}

function drawAxes() {
    context.strokeStyle = "#999999";
    context.beginPath();
    context.moveTo(canvas.width/2,0);
    context.lineTo(canvas.width/2,canvas.height);
    context.stroke();
    
    context.beginPath();
    context.moveTo(0,canvas.height/2);
    context.lineTo(canvas.width,canvas.height/2);
    context.stroke();
}

var points = [];
for (var i = 0; i < 1001; i++) {
    points[i] = Math.sqrt((i - 500)/100);//Math.pow(Math.cos((i - 500)/100), (i - 500)/100);
}
drawAxes();
drawGraph(points);