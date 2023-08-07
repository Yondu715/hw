const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d");

function line(x1, y1, x2, y2){
    const dx = x2 - x1;
    const dy = y2 - y1;
    const k = dy/dx;
    let x = x1;
    let y = y1;

    while (x <= x2){
        setPixel(x, y);
        y += Math.trunc(k);
        x++;
    }
}


function setPixel(x, y){
    const size = 5;
    ctx.fillStyle = "green";
    ctx.fillRect(x, y, size, size);
}

line(10, 200, 40, 100);