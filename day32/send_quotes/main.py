import smtplib
import datetime as dt
from random import choice


now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt") as fh:
        fh = fh.readlines()
        quote = choice(fh)
        quote = quote.strip()
    email = "sender@email.com"
    password = "app password"  # You have to create an app password for gmail to use here.
    with smtplib.SMTP("smtp.gmail.com") as conn: # and if not gmail, look for their server and replace
        conn.starttls()  # makes our connection secure
        conn.login(user=email, password=password)
        conn.sendmail(from_addr=email, to_addrs="receiver@email.com", msg=f"Subject:Motivational Quote\n\n{quote}")



