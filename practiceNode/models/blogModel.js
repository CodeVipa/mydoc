const mongoose =require('mongoose')
const schema=mongoose.Schema
const blogSchema=new schema({
    title:{
        type:String,
        required:true
    },
    content:{
        type:String,
        required:true
    },
    author:{
        type:String,
        required:true,
        
    }

})
//two parameters name and the schema
const Blog=mongoose.model('blog',blogSchema)

module.exports=Blog