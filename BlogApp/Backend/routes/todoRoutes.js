const controller = require('../controllers/todoController')

const express = require('express')
const router = express.Router()

router.get('/' ,  controller.faith)
router.get('/read' ,  controller.read)
router.put('/update' ,  controller.update)
router.delete('/delete' ,  controller.Delete)
// function expects 2 parameters
// route name  ,  function to be executed to that spesific  route

module.exports = router