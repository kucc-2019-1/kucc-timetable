const express = require('express')
const router  = express.Router()

const user = require('./db/user')
const time_slot = require('./db/time_slot')
const reservation = require('./db/reservation')


router.post('/', (req, res) => {
    console.log(req.body)
    res.json(req.body)
    // const newReseravtion = {
    //     name : req.body.data.name,
    //     title : req.body.data.title,
    //     day : req.body.data.day,
    //     start_time : req.body.data.start_time,
    //     end_time : req.body.data.end_time
    // }
    const newReseravtion = {
        title : "알고리즘 스터디",
        name : "남정호",
        day : "2019-05-06",
        start_time : 4,
        end_time : 5
    }

    var start_end_time_id = []
    for (s = newReseravtion.start_time; s <= newReseravtion.end_time; s++) {
        start_end_time_id.push(s)
    }

    var reserved_time_of_day = time_slot.filter(times => {
        return times.day === newReseravtion.day
    })

    //reserved == true -> 예약불가
    reserved = reserved_time_of_day.some(times => {
        return start_end_time_id.some(time_id => parseInt(times.time_index_id) === parseInt(time_id))
    })

    if(!reserved) {
        id = 7
        start_end_time_id.map(times => {
            time_slot.push({
                id : id,
                day : newReseravtion.day,
                time_index_id : times
            })
        })
        reservation.push({
            id : id,
            user_name : newReseravtion.name,
            title : newReseravtion.title
        })
    }

    console.log(reservation)
    console.log(time_slot)
})

module.exports = router