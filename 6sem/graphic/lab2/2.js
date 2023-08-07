const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d");
let width = canvas.offsetHeight;
let height = canvas.offsetHeight;

const leftBtn = document.getElementById("left");
const rightBtn = document.getElementById("right");
leftBtn.addEventListener("click", () => rotate(-45));
rightBtn.addEventListener("click", () => rotate(45));

let xPoints = [100, 100, 300];
let yPoints = [100, 300, 300];
drawTriangle(xPoints, yPoints);
xM = (xPoints[0] + xPoints[1] + xPoints[2]) / 3;
yM = (yPoints[0] + yPoints[1] + yPoints[2]) / 3;


function drawTriangle(xPoints, yPoints) {
	ctx.beginPath();
	ctx.moveTo(xPoints[0], yPoints[0]);
	ctx.lineTo(xPoints[1], yPoints[1]);
	ctx.lineTo(xPoints[2], yPoints[2]);
	ctx.closePath();
	ctx.stroke();
}

function rotate(angle){
	clear();
	let coords1 = getCoords(xPoints[0], yPoints[0], xM, yM, angle);
	let coords2 = getCoords(xPoints[1], yPoints[1], xM, yM, angle);
	let coords3 = getCoords(xPoints[2], yPoints[2], xM, yM, angle);
	xPoints = [coords1.x, coords2.x, coords3.x];
	yPoints = [coords1.y, coords2.y, coords3.y];
	drawTriangle(xPoints, yPoints);
}

function clear(){
	ctx.beginPath();
	ctx.rect(0, 0, width, height);
	ctx.fillStyle = "white";
	ctx.fill()
	ctx.closePath();
}

function getCoords(x, y, x0, y0, angle){
	xN = (x - x0) * Math.cos(angle * Math.PI / 180) - (y - y0) * Math.sin(angle * Math.PI / 180) + x0;
	yN = (x - x0) * Math.sin(angle * Math.PI / 180) + (y - y0) * Math.cos(angle * Math.PI / 180) + y0;
	return {
		x: xN,
		y: yN,
	}
}