import datetime
import time
import webbrowser

# Import the package which has the whatsapp web API
import pywhatkit as kit

# Let's open the whatsapp web if it is not open
# this is a pre-requisite for pywhatkit to work
# the browser should have whatsapp web open
webbrowser.open('https://web.whatsapp.com/')

# All the messages needed to be sent on a daily basis
msg = {
    0: """*LIVE* with *CaptainGaurav Monday at 7:00* AM using *Resistance Bands*  \
*Join here* : https://m.teamlink.co/  \
*Essentials* : Mini Resistance bands   \
*Level* : Intermediate \
_Please be ready with some basic warm up_""",

    1: """*LIVE with CaptainGaurav  Tuesday @ 7:00 AM*  for *Lower body* session  \
*Join here* : https://m.teamlink.co/   \
_Please be ready with some basic warm up_""",

    2: """The online session continues , *6:00am for Core n lower back*  \
*Join here* : https://m.teamlink.co/  \
*Essentials* : Yoga Mat/Bedsheet/Towel  Level : Elementary""",

    3: """*Thursday @ 7:00 AM*  for  *HIIT n Lower Body by CaptainGaurav*  \
*Join here* : https://m.teamlink.co/ \
*Level* : Intermediate  Please be ready with some basic warm up  \
*Workout details: 60 secs ON 15 secs OFF (beginners start with 45-30 secs then rest for 30-45 secs)  \
 3 rounds (continue in the break if you feel strong)*""",

    4: """Enjoy your break!!""",

    5: """Hope we enjoyed Friday Break !!  \
*LIVE* with *CaptainGaurav  Saturday @ 7:00 AM*  for  *ABS n Lower back* \
*Join here* :https://m.teamlink.co/ \
*Essentials* : Yoga Mat/Bedsheet/Towel \
*Level* : Elementary""",

    6: """Sunday Long run"""

}

# The group IDs in which the messages need to be forwarded
groups = ["group id 1", "group id 2"]

# Get the current date
now = datetime.datetime.now()

# Get the weekday number
# 0 : Monday
# 1 : Tuesday
day_num = now.weekday()

# Get the minute from current timestamp
now_minute = now.minute

for grp in groups:

    # Need to add 2 minutes to current time because this API has mechanism to wait for minimum 2 minutes before
    # hitting the API
    now_minute = now_minute + 2
    if now_minute >= 60:
        now_minute = now_minute - 60

    # This API hits the whatsapp web API, selects the particular group and sends message
    kit.sendwhatmsg_to_group(group_id=grp, message=msg[day_num + 1], time_hour=now.hour,
                             time_min=now_minute, wait_time=20, print_wait_time=True)
    # Message like the following should appear on terminal
    # In 95 seconds web.whatsapp.com will open and after 20 seconds message will be delivered

    # Sleep for 1 sec after sending message to one group
    time.sleep(1)
