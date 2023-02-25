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

// Create a new calender instance.
const calendar = google.calendar({ version: 'v3', auth: oAuth2Client })

// Create a new event start date instance for temp uses in our calendar.
const eventStartTime = new Date()
eventStartTime.setDate(eventStartTime.getDate()+3)

// Create a new event end date instance for temp uses in our calendar.
const eventEndTime = new Date()
eventEndTime.setDate(eventEndTime.getDate()+3)
eventEndTime.setMinutes(eventEndTime.getMinutes() + 45)

// Create a dummy event for temp uses in our calendar
const event = {
  summary: `Meeting with David`,
  description: `Meet with David to talk about the new client project and how to integrate the calendar for booking.`,
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

// Check if we a busy and have an event on our calendar for the same time.
calendar.freebusy.query(
    {
      resource: {
        timeMin: eventStartTime,
        timeMax: eventEndTime,
        timeZone: 'Asia/Singapore',
        items: [{ id: 'primary' }],
      },
    },
    (err, res) => {
      // Check for errors in our query and log them if they exist.
      if (err) return console.error('Free Busy Query Error: ', err)
  
      // Create an array of all events on our calendar during that time.
      const eventArr = res.data.calendars.primary.busy
  
      // Check if event array is empty which means we are not busy
      if (eventArr.length === 0)
        // If we are not busy create a new calendar event.
        return calendar.events.insert(
          { calendarId: 'primary', resource: event },
          err => {
            // Check for errors and log them if they exist.
            if (err) return console.error('Error Creating Calender Event:', err)
            // Else log that the event was created.
            return console.log('Calendar event successfully created.')
          }
        )
      // If event array is not empty log that we are busy.
      return console.log(`Sorry I'm busy...`)
    }
  )
