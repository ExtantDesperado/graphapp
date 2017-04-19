var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

function drawGraph(points) {
    context.beginPath();
    context.moveTo(0,canvas.height/2-points[0]*canvas.height/10);
    for (var i = 1; i < points.length; i++) {
        context.lineTo(i*canvas.width/10,canvas.height/2-points[i]*canvas.height/10);
    }
    context.stroke();
}

var points = [25,16,9,4,1,0,1,4,9,16,25];
/*var points = [];
for (var i = 0; i < 1001; i++) {
    points[i] = (i/100 - 5);
}*/
drawGraph(points);