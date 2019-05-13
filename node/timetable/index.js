const express = require('express');
const path = require('path');

const app = express();

// API routers
app.use('/day', require('./routers/api/dateListView'));
app.use('/times', require('./routers/api/availableReservationTimeView'));
app.use('/timetable', require('./routers/api/timeTableView'));
app.use('/reservation', require('./routers/api/makeReservation'));

//process.env.PORT를 먼저 확인한다는데 찾아보기
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`SERVER STARTED ON PORT ${PORT}`)); 