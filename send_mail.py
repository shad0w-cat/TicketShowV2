from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

SMTP_SERVER_HOST= "localhost"
SMTP_SERVER_PORT= 1025
SENDER_ADDRESS = "iamstuarttheminion@gmail.com"
SENDER_PASSWORD = "aplnoeailycvpgwg"

def send_email(to_address, subject, message):
    msg=MIMEMultipart()
    msg["From"] = SENDER_ADDRESS
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.attach(MIMEText(message,"html"))
    
    s = smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT)
    s.login(SENDER_ADDRESS,SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()
    return True 

    
# def main():
#     send_email("sample@gmail.com", subject="Test mail", message = "hi")

# if __name__=="__main__":
#     main()