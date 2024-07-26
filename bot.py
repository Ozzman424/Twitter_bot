import tweepy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, EMAIL_USER, EMAIL_PASSWORD

# Twitter authentication
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET_KEY,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# List of Twitter handles to monitor
twitter_handles = ['stock_handle_1', 'stock_handle_2', 'stock_handle_3']

# Email configuration
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, EMAIL_USER, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.screen_name in twitter_handles:
            subject = f"New Tweet from {status.user.screen_name}"
            body = status.text
            send_email(subject, body)

    def on_error(self, status_code):
        if status_code == 420:
            return False

def main():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    myStream.filter(follow=[str(api.get_user(screen_name=handle).id) for handle in twitter_handles])

if __name__ == "__main__":
    main()
