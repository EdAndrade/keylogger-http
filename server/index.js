const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = 3000

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.post('/', (req, res) => {
    res.send('ACK')
    console.log(req.body)
})

app.listen(port, () => console.log(`running in localhost:${port}`))