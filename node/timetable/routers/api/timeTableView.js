const express = require('express')
const router = express.Router()

const time_slot = require("./db/time_slot")
const reservation = require("./db/reservation")


router.get('/', (req, res) => {

    var date = new Date(); /* 현재 */
    var day_to_get = []
    for (i = 0; i < 14; i++) {
        date.setDate(date.getDate() + i);
        day_to_get.push(date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate())
    };

    data = []

    reservation_list = []

    time_slot.map(time => {
        for (i = 0; i < reservation.length; i++) {
            if (time.id === reservation[i].id) {
                reserved = {}
                reserved.id = time.id
                reserved.day = time.day
                reserved.time_index_id = time.time_index_id
                reserved.user_name = reservation[i].user_name
                reserved.title = reservation[i].title 
            }
        }
        reservation_list.push(reserved)
    })
    res.json(reservation_list)
})

module.exports = router