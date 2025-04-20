const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')//parse request and response in Json format
const cors = require('cors')//cross origin requests it allows certain origins to consume Apis
const port = 3000;
const router = require('./routes/todoRoutes')
const app = express()



//middlewares
app.use(cors());
app.use(bodyParser.json())
app.use('/',router)

app.listen(port , ()=>{
    console.log(`the server is running on http://localhost:${port}`)
})


app.use((req, res, next) => {
    console.log(req.method)
    next()
})

//connection to mongodb

try {
    connect = mongoose.connect('mongodb://localhost:27017/todolist')
    if(connect){
        console.log('Successifully connected to mongo db')
    }
} catch (error) {
    console.log(error)
}

//start the server

