const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d");
let width = canvas.offsetHeight;
let height = canvas.offsetHeight;
let rect, circle, triangle = false;

let addButtons = document.getElementsByClassName("adding");
let deleteButtons = document.getElementsByClassName("deleting");

for (let i = 0; i < addButtons.length; i++) {
	const element = addButtons[i];
	element.addEventListener("click", addFigure);
}

for (let i = 0; i < deleteButtons.length; i++) {
	const element = deleteButtons[i];
	element.addEventListener("click", deleteFigure);
}

function addFigure(event){
	const target = event.target;
	const figure = target.closest(".figure");
	const figureName = figure.childNodes[1].textContent;
	ctx.strokeStyle = "black";
	if (figureName == "Квадрат") drawRect();
	if (figureName == "Круг") drawCircle();
	if (figureName == "Треугольник") drawTriangle();
}

function deleteFigure(event){
	const target = event.target;
	const figure = target.closest(".figure");
	const figureName = figure.childNodes[1].textContent;
	ctx.beginPath();
	ctx.rect(0, 0, width, height);
	ctx.fillStyle = "white";
	ctx.fill()
	if (figureName == "Квадрат") clearRect();
	if (figureName == "Круг") clearCircle();
	if (figureName == "Треугольник") clearTriangle();
}

function drawRect(){
	ctx.strokeRect(100, 100, width/2, height/2);
	rect = true;
}

function clearRect(){
	rect = false;
	if (circle == true) drawCircle();
	if (triangle == true) drawTriangle();
}

function drawCircle(){
	ctx.beginPath();
	ctx.arc(300, 200, width/4, 0, 2 * Math.PI);
	ctx.closePath();
	ctx.stroke();
	circle = true;
}

function clearCircle(){
	circle = false;
	if (rect == true) drawRect();
	if (triangle == true) drawTriangle();
}

function drawTriangle(){
	triangle = true;
	ctx.beginPath();
	ctx.moveTo(100, 100);
	ctx.lineTo(100, 300);
	ctx.lineTo(300, 300);
	ctx.closePath();
	ctx.stroke();
}

function clearTriangle(){
	triangle = false;
	if (rect == true) drawRect();
	if (circle == true) drawCircle();
}