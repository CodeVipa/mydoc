const mongoose = require('mongoose')

todoschema = mongoose.Schema({
    // title:{
    //     type:String,
    //     require:true,   //not null
    //     unique:true,
    //     created_at:date , default:Date.now() ,
    // }

    task:{
        type:String
    }
})

const Todo = mongoose.model('tasks' , todoschema)

module.exports = Todo