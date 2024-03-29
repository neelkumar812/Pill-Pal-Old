const {google} = require('googleapis')
// const { oauth2 } = require('googleapis/build/src/apis/oauth2')

const { OAuth2 } = google.auth

const oAuth2Client = new OAuth2(
    '1068371688536-o9pbcmu2ugtg77c53f8acn9ini27lkh2.apps.googleusercontent.com',
    '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'
)

oAuth2Client.setCredentials({refresh_token:
     '1//04qLiXt_6Q8KUCgYIARAAGAQSNwF-L9IrJZdEEIMKwpv52ClCGbrV02Ce3-LrN5sSrK9IYbqtCw0YQjMb-TMaeoBfwqBXREwxcNs'
})

//loading data file
const presc = require('../runner/presc.json')
console.log(presc);


// Create a new calender instance.
const calendar = google.calendar({ version: 'v3', auth: oAuth2Client })

// Create a new event start date instance for temp uses in our calendar.
const eventStartTime = new Date()
const eventEndTime = new Date()

eventStartTime.setDate(eventStartTime.getDate())
eventStartTime.setHours(eventStartTime.getHours()-4)
// Create a new event end date instance for temp uses in our calendar.
eventEndTime.setDate(eventEndTime.getDate())
eventEndTime.setHours(eventEndTime.getHours()-4)
eventEndTime.setMinutes(eventEndTime.getMinutes() + 45)

var event = {
  summary: `Take your medicine!`,
  description: `Take ${presc[1]} pill of ${presc[0]}, ${presc[2]} times a day`,
  colorId: 1,
  start: {
    dateTime: eventStartTime,
    timeZone: 'Asia/Singapore',
  },
  end: {
    dateTime: eventEndTime,
    timeZone: 'Asia/Singapore',
  },
}

calendar.events.insert(
  {calendarId: 'primary',
  resource: event})

require('./index2.js')

// calendar.freebusy.query(
// {
//   resource: {
//     timeMin: eventStartTime,
//     timeMax: eventEndTime,
//     timeZone: 'Asia/Singapore',
//     items: [{ id: 'primary' }],
//   },
// },
// (err, res) => {
//   // Check for errors in our query and log them if they exist.
//   if (err) return console.error('Free Busy Query Error: ', err)

//   // Create an array of all events on our calendar during that time.
//   const eventArr = res.data.calendars.primary.busy

//   // Check if event array is empty which means we are not busy
//   if (eventArr.length === 0)
//     // If we are not busy create a new calendar event.
//     return calendar.events.insert(
//       { calendarId: 'primary', resource: event },
//       err => {
//         // Check for errors and log them if they exist.
//         if (err) return console.error('There was an error in creating the calendar event: ', err)
//         // Else log that the event was created.
//         return console.log('Event has been successfully created.')
//       }
//     )
//   // If event array is not empty log that we are busy.
//   return console.log(`Sorry I'm busy...`)
// }
// )



// Create a dummy event for temp uses in our calendar


// Check if we a busy and have an event on our calendar for the same time.
