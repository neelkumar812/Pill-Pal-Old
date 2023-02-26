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
//console.log(presc);


// Create a new calender instance.
const calendar = google.calendar({ version: 'v3', auth: oAuth2Client })

// Create a new event start date instance for temp uses in our calendar.
const eventStartTime = new Date()
const eventEndTime = new Date()

eventStartTime.setDate(eventStartTime.getDate())
eventStartTime.setHours(eventStartTime.getHours()+6)

// Create a new event end date instance for temp uses in our calendar.
eventEndTime.setDate(eventEndTime.getDate())
eventEndTime.setHours(eventEndTime.getHours()+6)
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

return console.log('Event has been successfully created.')
