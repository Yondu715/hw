const express = require('express');
const fs = require('fs');
const XSS_SYMBOLS = [/&/g, /</g, />/g, /"/g, /'/g];
const XSS_SAVE = ["&amp;", "&lt;", "&gt;", "&quot;", "&#039;"];

const app = express();

app.use(express.static('public'));
app.use(express.json())

const checkRequestBody = (json) => {
    const keys = Object.keys(json);
    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const payload = json[key];
        for (let j = 0; j < XSS_SYMBOLS.length; j++) {
            const symbol = XSS_SYMBOLS[j];
            if (symbol.test(payload)) return false;
        }
    }
    return true;
}

const escapeHtml = (unsafe) => {
    let saveStr = unsafe;
    for (let i = 0; i < XSS_SYMBOLS.length; i++) {
        const symbol = XSS_SYMBOLS[i];
        const symbolSave = XSS_SAVE[i];
        saveStr = saveStr.replace(symbol, symbolSave);
    }
    return saveStr;
}

app.get('/file', function (request, response) {
    fs.readFile('file.txt', 'utf8', function (error, fileContent) {
        if (error) throw error;
        response.end(escapeHtml(fileContent));
    });
});

app.post('/file', function (request, response) {
    if (!checkRequestBody(request.query)) {
        response.status(500);
        return response.end('Небезопасное содержимое запроса');
    };
    fs.readFile('file.txt', 'utf8', function (error, fileContent) {
        const toWrite = `${fileContent}\ntitle: ${request.body.title}\ntext: ${request.body.text}\n`;
        fs.writeFile('file.txt', toWrite, function (error) {
            if (error) throw error;
            console.log('Данные успешно записаны');
        });
    });
    response.end('ok');
})

app.listen(3000);