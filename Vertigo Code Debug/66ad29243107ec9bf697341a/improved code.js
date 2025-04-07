const moment = require("moment-timezone")

const getDifferenceInHHMM = (dateTimeStr1, dateTimeStr2) => {
    const duration = moment.duration(moment(dateTimeStr1).diff(moment(dateTimeStr2)))
    const totalMinutes = Math.abs(duration.asMinutes())
    return `${String(Math.floor(totalMinutes / 60)).padStart(2, "0")}:${String(totalMinutes % 60).padStart(2, "0")}`
}

const dateTimeStr1 = "2024-08-02T15:30:00+00:00"
const dateTimeStr2 = "2024-08-01T14:30:00+01:00"
console.log(getDifferenceInHHMM(dateTimeStr1, dateTimeStr2))