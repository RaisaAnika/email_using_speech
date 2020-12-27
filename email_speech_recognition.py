import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer() #to listen from microphone

def get_msg(): #listening function
    try:
        with sr.Microphone as source:
            print('listening...')
            voice = listener.listen(source)
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
        return info.lower() #convert all text to lower case
    except:
        pass

def simple_email():
    server = smtplib.SMTP('smtp.gmail.com',587) #if sender account is gmail
    server.starttls()
    server.login('youremail@gmail.com','yourpassword')
    server.sendmail('youremail@gmail.com','reciver@mars.com','hi I am an automatic sender') #note your account should have the permisssion to send automail

## this would take params sent by get_email_info() and then send the mail as desired
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access to the sender account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {  #to map email ids to users
    'master': 'master_EMAIL',
    'Diamond': 'diamond@hogwarts.com',
    'Jennie': 'jennie@hogwarts.com',
    'Alisa': 'alisa@tvd.com',
    'irene': 'irene@gmail.com'
}
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_email_info():
    talk('To Whom you want to send email')
    name = get_msg()
    receiver = email_list[name] #get the e-mail id against the name in email list
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_msg()
    talk('What will be in your email body')
    message = get_msg()
    send_email(receiver, subject, message) #sending parameter to function send_email
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_msg()
    if 'yes' in send_more:
        get_email_info()


get_email_info()