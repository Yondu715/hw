const express = require('express');
const path = require('path');

const app = express();

app.use('/form', express.static(path.join(__dirname, 'public/bad')));

app.listen(3001);