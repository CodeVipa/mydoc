const express=require('express')
const app=express()
const mongoose=require('mongoose')
const router=require('./routes/blogRoutes')
app.listen(2000,()=>{
    console.log('connected successfully!')
})

mongoose.connect('mongodb://localhost:27017/Blogflix')

app.use(router)