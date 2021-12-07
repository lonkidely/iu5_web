'use strict';

const express = require('express');
const path = require('path');
const app = express();
const htmlPath = path.resolve(__dirname, '../public/index.html');
const staticPath = path.resolve(__dirname, '../src');
const port = 9160;

app.use('/', express.static(staticPath));

app.all('*', (req, res) => {
    res.sendFile(htmlPath);
});

app.listen(port, () => {
    console.log('Server listening http://localhost:${port}');
});

