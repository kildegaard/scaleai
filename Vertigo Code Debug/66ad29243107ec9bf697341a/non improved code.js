function parseDateTime(dateTimeStr) {
    const dateTime = new Date(dateTimeStr)
    const tzOffset = -dateTime.getTimezoneOffset()
    const year = dateTime.getUTCFullYear()
    const month = dateTime.getUTCMonth() + 1
    const day = dateTime.getUTCDate()
    const hour = dateTime.getUTCHours()
    const minute = dateTime.getUTCMinutes()

    return { year, month, day, hour, minute, tzOffset }
}

function convertToUTC(dateTime) {
    const { year, month, day, hour, minute, tzOffset } = dateTime
    const totalMinutes = Date.UTC(year, month - 1, day, hour, minute) / 60000
    const utcMinutes = totalMinutes - tzOffset
    return utcMinutes
}

function getDifferenceInHHMM(dateTimeStr1, dateTimeStr2) {
    const dateTime1 = parseDateTime(dateTimeStr1)
    const dateTime2 = parseDateTime(dateTimeStr2)

    const utcMinutes1 = convertToUTC(dateTime1)
    const utcMinutes2 = convertToUTC(dateTime2)

    const diffMinutes = Math.abs(utcMinutes2 - utcMinutes1)
    const diffHours = Math.floor(diffMinutes / 60)
    const remainingMinutes = diffMinutes % 60

    return `${String(diffHours).padStart(2, '0')}:${String(remainingMinutes).padStart(2, '0')}`
}

const dateTimeStr1 = "2024-08-02T15:30:00+00:00"
const dateTimeStr2 = "2024-08-01T14:30:00+01:00"
console.log(getDifferenceInHHMM(dateTimeStr1, dateTimeStr2))