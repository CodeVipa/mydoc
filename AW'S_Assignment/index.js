const express=require('express')
const mongoose=require('mongoose')
const app=express()
const router=require('./routes/stockRoute')

app.listen(2500,()=>{
    console.log('listening to the port 2500')
})

mongoose.connect('mongodb://localhost:27017/StockMs')

app.use(router)