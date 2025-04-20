const Todo=require('../models/Todo')
//create or add
const faith = async(req,res)=>{
    const task='hello'
    const new_task=Todo({task})
    await new_task.save()
    res.send(`it has been saved successfully`)
}
//read
const read = async(req,res)=>{
   const data= await Todo.find({task:'hello'})
   res.send(data)
}
//update
const update = async(req,res)=>{
    const data= await Todo.find({task:'faith'})
    const ids = data[0]._id
    const toreplace = {task : "frank"}
    const updated_data = await Todo.findByIdAndUpdate(ids, toreplace)
    res.send(updated_data)
}

const Delete = async (req,res)=>{
    const datas = await Todo.find({task:'frank'})
    const deleted_data = await Todo.findOneAndDelete(datas)
    res.send(deleted_data)
}
module.exports={faith,read , update,Delete}