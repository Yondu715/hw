const express = require('express');
const path = require('path');
const session = require('express-session');
// const badRouter = require('./bad-server');

const app = express();

app.use(session({
    secret: "YkJG14aZdy4T",
    cookie: {
        maxAge: 600000,
        domain: '.',
        httpOnly: true
    }
}));

app.use(express.urlencoded({ extended: true }));

// app.use('/bad', badRouter);

app.use('/auth/login', express.static(path.join(__dirname, 'public/auth')));

app.post('/auth/login', function (request, response) {
    if (request.session) {
        request.session.user = {
            username: request.body.username,
            password: request.body.password
        };
    }
    return response.redirect('/auth/login');
});

app.get('/auth/me', function (request, response) {
    if (request.session) {
        console.log(request.session);
        return response.send(JSON.stringify(request.session.user));
    }
    return response.status(401).send();
});

app.listen(3000);