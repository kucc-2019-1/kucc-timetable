const express = require('express')
const router = express.Router()


router.get('/', (req, res) => {
    date = new Date()

    const dictionary = [{
        "message": "",
        "data": {"day": date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate(), "day_of_week": date.getDay()}
    }]
    res.json(dictionary)
})

module.exports = router;
