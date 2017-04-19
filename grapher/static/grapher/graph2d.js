var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

function Point2D(x,y) {
    this.x = x;
    this.y = y;
}

function drawGraph(points) {
    context.beginPath();
    context.moveTo(0,points[0]*10);
    for (var i = 1; i < points.length; i++) {
        context.lineTo(i*10,points[i]*10);
    }
    context.stroke();
}

var points = [16,9,4,1,0,1,4,9,16];
drawGraph(points);