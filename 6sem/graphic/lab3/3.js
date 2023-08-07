const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d");
const width = canvas.offsetWidth;
const height = canvas.offsetHeight;

const screen_x0 = width / 6;
const screen_x1 = screen_x0 + 500;
const screen_y0 = height / 4;
const screen_y1 = screen_y0 + 300;

const upBtn = document.getElementById("up");
const downBtn = document.getElementById("down");
const leftBtn = document.getElementById("left");
const rightBtn = document.getElementById("right");
upBtn.addEventListener("click", () => move(0, -10));
downBtn.addEventListener("click", () => move(0, 10));
leftBtn.addEventListener("click", () => move(-10, 0));
rightBtn.addEventListener("click", () => move(10, 0));


let src = [[200, 150], [200, 350], [400, 350]];
let n = src.length;

clear();
draw(src);

function draw(src) {
	ctx.beginPath();
	if (src[0]) {
		ctx.moveTo(src[0][0], src[0][1]);
	}
	for (let index = 1; index < src.length; index++) {
		ctx.lineTo(src[index][0], src[index][1]);
	}
	ctx.closePath();
	ctx.stroke();
}

function move(x, y) {
	for (let i = 0; i < src.length; i++) {
		src[i][0] += x;
		src[i][1] += y;
	}
	clear();
	let dst = clip(src);
	draw(dst);
}

function clip(src) {
	let dst = [];
	let newS = src.slice();
	let funcs = [clipDown, clipLeft, clipRight, clipUp];
	for (let i = 0; i < funcs.length; i++) {
		funcs[i](dst, newS);
		newS = dst.slice();
		dst.length = 0;
	}
	return newS;
}

function clipRight(dst, src) {
	let r = 0;
	for (let i = 0; i < src.length; i++) {
		let p1 = src[i];
		let p2 = src[(i + 1) % src.length];
		if (p1[0] <= screen_x1) {
			dst[r++] = p1;
		}
		if ((p1[0] < screen_x1 && p2[0] > screen_x1) || (p2[0] <= screen_x1 && p1[0] > screen_x1)) {
			let y = p2[1] + (screen_x1 - p2[0]) / (p1[0] - p2[0]) * (p1[1] - p2[1]);
			let x = screen_x1;
			dst[r] = [x, y];
			r++;
		}
	}
}

function clipLeft(dst, src) {
	let r = 0;
	for (let i = 0; i < src.length; i++) {
		let p1 = src[i];
		let p2 = src[(i + 1) % src.length];
		if (p1[0] >= screen_x0) {
			dst[r++] = p1;
		}
		if ((p1[0] > screen_x0 && p2[0] < screen_x0) || (p2[0] >= screen_x0 && p1[0] < screen_x0)) {
			let y = p1[1] + (screen_x0 - p1[0]) / (p2[0] - p1[0]) * (p2[1] - p1[1]);
			let x = screen_x0;
			dst[r] = [x, y];
			r++;
		}
	}
}

function clipUp(dst, src) {
	let r = 0;
	for (let i = 0; i < src.length; i++) {
		let p1 = src[i];
		let p2 = src[(i + 1) % src.length];
		if (p1[1] >= screen_y0) {
			dst[r++] = p1;
		}
		if ((p1[1] > screen_y0 && p2[1] < screen_y0) || (p2[1] >= screen_y0 && p1[1] < screen_y0)) {
			let x = p1[0] + (screen_y0 - p1[1]) / (p2[1] - p1[1]) * (p2[0] - p1[0]);
			let y = screen_y0;
			dst[r] = [x, y];
			r++;
		}
	}
}

function clipDown(dst, src) {
	let r = 0;
	for (let i = 0; i < src.length; i++) {
		let p1 = src[i];
		let p2 = src[(i + 1) % src.length];
		if (p1[1] <= screen_y1) {
			dst[r++] = p1;
		}
		if ((p1[1] < screen_y1 && p2[1] > screen_y1) || (p2[1] <= screen_y1 && p1[1] > screen_y1)) {
			let x = p2[0] + (screen_y1 - p2[1]) / (p1[1] - p2[1]) * (p1[0] - p2[0]);
			let y = screen_y1;
			dst[r] = [x, y];
			r++;
		}
	}
}


function clear() {
	ctx.beginPath();
	ctx.rect(0, 0, width, height);
	ctx.fillStyle = "white";
	ctx.fill()
	ctx.closePath();
	ctx.strokeRect(screen_x0, screen_y0, 500, 300);
}
