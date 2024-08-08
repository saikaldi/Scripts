import smtplib
import os


def send_email(message):
    sender = "ukyzsaikal@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        # logging on to the server
        server.login(sender, password)

        # sending the email
        server.sendmail(sender, sender, message)

        return "The was message was sent succefully"
    except Exception as ex:
        return f"Error: {ex}\nCheck your login or password please"


def main():
    message = input("Type your message")
    print(send_email(message))


if __name__ == "__main__":
    main()
