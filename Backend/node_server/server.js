import express from 'express';
import { parse } from 'url';
import { parse as parseQuery } from 'querystring';
import {brx_image_generator} from './index.mjs'
const app = express();

const PORT = 3000;

app.get('/user_prompt', async (req, res) => {
    const parsedUrl = parse(req.url);

    // Get the query string
    const queryString = parsedUrl.query;

    // Parse the query string to get the parameters
    const queryParams = parseQuery(queryString);

    // Get the value of the 'user_prompt' parameter
    const userPromptValue = queryParams.user_prompt;
    console.log(userPromptValue)
    //res.send({"data":"test data"})
    const responseData = await brx_image_generator(userPromptValue)
    console.log(responseData)
    res.send(responseData);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});