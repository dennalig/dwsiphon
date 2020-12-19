//Express Hello World Ex: https://expressjs.com/en/starter/hello-world.html
const express = require('express'); // importing express
const app = express();
const port = 5000; // change from 3000 5000 as 3000 is where react is ran
// start with node app.js

app.get('/', (req, res) => {
  res.send('Hello World!')
});


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});

//https://www.youtube.com/watch?v=kJA9rDX7azM&t=481s