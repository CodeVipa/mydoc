const Blog=require('../models/blogModel')

const index=(req,res)=>{
    res.json('hello faith')
}


//any operation u do in model returns promise

const getAllblogs=async(req,res)=>{
    //finding all the blogs we have in database
    const blogs=await Blog.find()
    res.json(blogs)
}
//finding a certain blog by id
const getOneBlog=async(req,res)=>{
    const id = req.params.id  //we are getting id from the requests
    const oneBlog=await Blog.findById(id)
    res.json(oneBlog)
}

module.exports={
    index,
    getAllblogs,
    getOneBlog,
}