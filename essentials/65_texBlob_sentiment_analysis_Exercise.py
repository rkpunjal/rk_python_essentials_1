# Plot: Fictional story: In a Dystopian society, certain organizations have sort of enslaved. At the end of day,
# after work, before leaving each person is supposed to enter a positive feeling statement about their workplace.
# The system will keep on asking them for a positive statement.
# If a negative statement is entered, they will be asked again, until a positive statement is entered.

import pyttsx3 # for Text-to-Speech
import textblob # for text sentiment analysis


def init_TTY_engine():
    global engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('voice',
                       "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0")


def say(msg):
    engine.say(msg)
    engine.runAndWait()


def get_polarity(statement):
    blob = textblob.TextBlob(statement)
    return blob.sentiment.polarity


init_TTY_engine()
employee_number = 2215674
msg = f"Employee Number {employee_number}, We hope you had a great day of work. It's time to submit your employee Wellness Statement."
say(msg)

polarity = 0
while polarity < 0.3:
    statement = input("Enter your Employee wellness statement here : ")
    polarity = get_polarity(statement)
    # print("sentiment : ", polarity)

    if polarity < 0.3:
        msg = f'''Employee Number {employee_number}, that was not a very positive statement.
        Please try again and be more positive this time. We know how much you love working here.'''
        say(msg)

msg = f"Thank you, and we appreciate for your response! 'Employee Number {employee_number} You are now granted the permission to leave!"
say(msg)
