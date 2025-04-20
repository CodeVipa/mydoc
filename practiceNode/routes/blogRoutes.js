const BlogController=require('../controllers/blogController')
const express = require('express')
const router=express.Router()
router.get('/index',BlogController.index)
router.get('/show',BlogController.getAllblogs)
router.get('/show/:id',BlogController.getOneBlog)

module.exports=router