import express from 'express';
import { parse } from 'url';
import { parse as parseQuery } from 'querystring';
import {brx_image_generator} from './index.mjs'
const app = express();

const PORT = 3000;

app.get('/user_prompt', (req, res) => {
    const parsedUrl = parse(req.url);

    // Get the query string
    const queryString = parsedUrl.query;

    // Parse the query string to get the parameters
    const queryParams = parseQuery(queryString);

    // Get the value of the 'user_prompt' parameter
    const userPromptValue = queryParams.user_prompt;
    console.log(userPromptValue)
    res.send(brx_image_generator(userPromptValue));
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});