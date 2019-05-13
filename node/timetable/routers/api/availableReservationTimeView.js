const express = require('express')
const router = express.Router()

const time_slot = require('./db/time_slot')

router.get('/', (req, res)=>{

    // var day = req.body.day || null
    var day = "2019-05-06"
    var unableTimes = time_slot.filter(times => times.day === day)
    const countindex = 9
    var order = []
    for (i = 0; i < countindex; i++) {
        order.push(i)
    }
    unableTimes.map(times => {
        order.splice(order.indexOf(times.time_index_id),1)
    })
    console.log(order)

    data = []
    order.map(time_index_id => {
        dict = {"order" : time_index_id}
        //"time" 객체 추가해야
        // dict = {"order" : time_index_id, "time": str(models.TimeIndex.objects.get(time_index_id=i)}
        data.push(dict)
    })

    dictionary = [
        {
            "message" : "",
            "data" : data
        }   
    ]

    res.json(dictionary)
})

module.exports = router
