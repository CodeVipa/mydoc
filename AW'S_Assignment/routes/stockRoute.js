// const { Route } = require('react-router-dom')
const Stockcontroller=require('../controllers/stockController')
const express=require('express')
const router=express.Router()

router.get('/index',Stockcontroller.index)

module.exports=router