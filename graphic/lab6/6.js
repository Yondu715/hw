const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d");


function setPixel(x, y) {
    const size = 5;
    ctx.fillStyle = "green";
    ctx.fillRect(x, y, size, size);
}

function setPixel14(Cx, Cy, R) {
    setPixel(Cx, Cy + R);
    setPixel(Cx, Cy - R);
    setPixel(Cx + R, Cy);
    setPixel(Cx - R, Cy);
}

function setPixel18(Cx, Cy, x, y) {
    setPixel(Cx + x, Cy + y);
    setPixel(Cx - x, Cy + y);
    setPixel(Cx + x, Cy - y);
    setPixel(Cx - x, Cy - y);
    setPixel(Cx + y, Cy + x);
    setPixel(Cx - y, Cy + x);
    setPixel(Cx + y, Cy - x);
    setPixel(Cx - y, Cy - x);
}

function circle(Cx, Cy, R) {
    let f = 1 - R;
    let x = 0;
    let y = R;
    let incrE = 3;
    let incrSE = 5 - 2 * R;
    setPixel14(Cx, Cy, R);
    while (x <= y) {
        if (f > 0) {
            y -= 1;
            f += incrSE;
            incrSE += 4;
        }
        else {
            f += incrE;
            incrSE += 2;
        }
        incrE += 2;
        x += 1;
        setPixel18(Cx, Cy, x, y);
    }
}

circle(250, 250, 100);
