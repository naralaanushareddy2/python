import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime, timedelta
import threading
import time
import re
from playsound import playsound
from plyer import notification

# --------------------------------------------------
# CREATE OBJECTS
# --------------------------------------------------

recogniser = sr.Recognizer()
engine = pyttsx3.init()


# --------------------------------------------------
# LISTEN FUNCTION
# --------------------------------------------------

def listen():
    print('Listening....')

    with sr.Microphone() as microphone:
        audio = recogniser.listen(microphone)

    try:
        text = recogniser.recognize_google(audio)
        print('You:', text)
        return text.lower()

    except sr.UnknownValueError:
        print('Sorry, I cannot understand you...')
        return ''

    except sr.RequestError:
        print('Unable to connect speech recognition service')
        return ''


# --------------------------------------------------
# SPEAK FUNCTION
# --------------------------------------------------

def speak(text):
    print('Assistant:', text)
    engine.say(text)
    engine.runAndWait()


# --------------------------------------------------
# ALARM FUNCTION
# --------------------------------------------------

def set_alarm(alarm_time):

    print(
        'Alarm waiting for:',
        alarm_time.strftime('%I:%M %p')
    )

    while True:

        current_time = datetime.now()

        if current_time >= alarm_time:

            speak('Alarm! Your alarm time has arrived.')

            try:
                playsound('alarm.mp3')

            except Exception as error:
                print(
                    'Could not play alarm sound:',
                    error
                )

            break

        time.sleep(1)

 
# --------------------------------------------------
# CREATE ALARM TIME
# --------------------------------------------------

def create_alarm_time(time_text):

    time_text = time_text.lower()

    # Convert "p.m." to "pm"
    time_text = time_text.replace('.', '')

    # Supports:
    # 9 pm
    # 9:40 pm
    # 9 40 pm
    # 9:25 p.m.

    pattern = r'(?:on\s+)?([a-zA-Z]+\s+\d{1,2}(?:st|nd|rd|th)?)(?:\s+at\s+|\s+)(\d{1,2})(?::(\d{2}))?\s*(am|pm)\s+to\s+(.+)'

    match = re.search(pattern, reminder_text)

    if match:

        date_text = match.group(1)

        date_text = re.sub(
            r'(st|nd|rd|th)$',
            '',
            date_text
        )

        hour = int(match.group(2))
        minute = int(match.group(3)) if match.group(3) else 0
        period = match.group(4)
        task = match.group(5)

    if not match:
        return None

    # Get hour
    hour = int(match.group(1))

    # Get minute
    if match.group(2):
        minute = int(match.group(2))
    else:
        minute = 0

    # Get AM / PM
    period = match.group(3)

    # Validate hour
    if hour < 1 or hour > 12:
        return None

    # Validate minute
    if minute < 0 or minute > 59:
        return None

    # Convert 12-hour time to 24-hour time

    if period == 'pm' and hour != 12:
        hour += 12

    elif period == 'am' and hour == 12:
        hour = 0

    # Get current date and time
    now = datetime.now()

    # Create alarm time
    alarm_time = now.replace(
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0
    )

    # If the alarm time has already passed today,
    # set it for tomorrow
    if alarm_time <= now:
        alarm_time += timedelta(days=1)

    return alarm_time


# ----------------------------------------------------
# SET REMAINDER
# -------------------------------------------------------------
def set_reminder(reminder_time, task):

    print(
        'Reminder waiting for:',
        reminder_time.strftime('%d %B %Y, %I:%M %p')
    )

    while True:

        current_time = datetime.now()

        if current_time >= reminder_time:

            # Voice reminder
            speak('Reminder! ' + task)

            # Windows notification
            notification.notify(
                title='EduLearn Reminder',
                message=task,
                timeout=10
            )

            break

        time.sleep(1)


# --------------------------------------------------
# ASSISTANT STARTS
# --------------------------------------------------

print('Welcome to Voice Assistant')


while True:

    command = listen()


    # --------------------------------------------------
    # HELLO
    # --------------------------------------------------

    if 'hello' in command:

        speak(
            'Hello, how can I help you?'
        )


    # --------------------------------------------------
    # TIME
    # --------------------------------------------------

    elif 'time' in command:

        current_time = datetime.now().strftime(
            '%I:%M %p'
        )

        speak(
            'The time is ' + current_time
        )


    # --------------------------------------------------
    # OPEN GOOGLE
    # --------------------------------------------------

    elif 'open google' in command:

        speak('Opening Google')

        webbrowser.open(
            'https://www.google.com'
        )


    # --------------------------------------------------
    # PLAY YOUTUBE
    # --------------------------------------------------

    elif command.startswith('play'):

        video = command.replace(
            'play',
            '',
            1
        ).strip()

        if video:

            speak(
                'Searching YouTube for ' + video
            )

            url = (
                'https://www.youtube.com/results?search_query='
                + video.replace(' ', '+')
            )

            webbrowser.open(url)

        else:

            speak(
                'Please tell me what you want to play'
            )


    # --------------------------------------------------
    # SET ALARM
    # --------------------------------------------------

    elif command.startswith('set alarm'):

        # Remove "set alarm"
        alarm_text = command.replace(
            'set alarm',
            '',
            1
        ).strip()

        # Remove "for"
        #
        # Example:
        # set alarm for 9:40 PM
        #
        # becomes:
        # 9:40 PM

        if alarm_text.startswith('for '):

            alarm_text = alarm_text.replace(
                'for ',
                '',
                1
            ).strip()

        # Convert spoken time into datetime
        alarm_time = create_alarm_time(
            alarm_text
        )

        if alarm_time:

            formatted_time = alarm_time.strftime(
                '%I:%M %p'
            )

            speak(
                'Alarm set for ' + formatted_time
            )

            # Start alarm in background
            alarm_thread = threading.Thread(
                target=set_alarm,
                args=(alarm_time,),
                daemon=True
            )

            alarm_thread.start()

        else:

            speak(
                'Sorry, I could not understand '
                'the alarm time. Please say '
                'something like set alarm for '
                '9 PM or 9:40 PM.'
            )
            
    # ----------------------------------
        # set remiander 
        # -------------------------------------------
    elif command.startswith('remind me'):

        reminder_text = command.replace('remind me', '', 1).strip()

        print('Reminder command:', reminder_text)

    # Example:
    # remind me on october 5 at 6:30 pm to submit assignment

        pattern = r'(?:on\s+)?([a-zA-Z]+\s+\d{1,2}(?:st|nd|rd|th)?)(?:\s+at\s+|\s+)(\d{1,2})(?::(\d{2}))?\s*(am|pm)\s+to\s+(.+)'
        

        match = re.search(pattern, reminder_text)

        if match:

            date_text = match.group(1)
            date_text = re.sub(
                r'(st|nd|rd|th)$',
                '',
                date_text
            )
            hour = int(match.group(2))
            minute = int(match.group(3)) if match.group(3) else 0
            period = match.group(4)
            task = match.group(5)

        # Convert AM/PM
            if period == 'pm' and hour != 12:
                hour += 12
            elif period == 'am' and hour == 12:
                hour = 0

            try:

                current_year = datetime.now().year

                reminder_time = datetime.strptime(
                    f'{date_text} {current_year}',
                    '%B %d %Y'
                )

                reminder_time = reminder_time.replace(
                    hour=hour,
                    minute=minute,
                    second=0,
                    microsecond=0
                )

            # If date/time already passed, use next year
                if reminder_time <= datetime.now():

                    reminder_time = reminder_time.replace(
                        year=current_year + 1
                    )

                speak(
                    'Reminder set for '
                    + reminder_time.strftime('%d %B at %I:%M %p')
                    + 'to '
                    + task
                )

                reminder_thread = threading.Thread(
                    target=set_reminder,
                    args=(reminder_time, task),
                    daemon=True
                )

                reminder_thread.start()

            except ValueError:

                speak(
                    'Sorry, I could not understand the date.'
            )

        else:

            speak(
                'Please say the reminder like '
                'remind me on October 5 at 6:30 PM '
                'to submit my assignment.'
            )     


    # --------------------------------------------------
    # GOOGLE SEARCH
    # --------------------------------------------------

    elif command.startswith('search'):

        search_text = command.replace(
            'search',
            '',
            1
        ).strip()

        if search_text:

            speak(
                'Searching for ' + search_text
            )

            url = (
                'https://www.google.com/search?q='
                + search_text.replace(' ', '+')
            )

            webbrowser.open(url)

        else:

            speak(
                'Please tell me what you want to search'
            )
    

    # --------------------------------------------------
    # EXIT
    # --------------------------------------------------

    elif (
        'exit' in command
        or 'quit' in command
        or 'stop' in command
    ):

        speak('Goodbye')

        break
    