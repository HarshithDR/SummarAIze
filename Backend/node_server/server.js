import express from 'express';
//import {brxObject} from './index.mjs'
const app = express();

const PORT = 3000;

app.get('/user_prompt', (req, res) => {

    res.send('Hello, World!');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});