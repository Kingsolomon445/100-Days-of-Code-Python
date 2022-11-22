import smtplib
import pandas as pd
from random import choice
import datetime as dt

#   Update the csv and save the details of their birthdays

EMAIL = "PUT YOUR EMAIL HERE"
PASSWORD = "PASS WORD"  # You have to create an app password to use here. Don't use the regular pass

today = dt.datetime.now()
day, month = today.day, today.month
bday_df = pd.read_csv("birthdays.csv")
for idx in bday_df.index:
    if bday_df.iloc[idx]["day"] == day and bday_df.iloc[idx]["month"] == month:  # if birthday is today
        num = choice([1, 2, 3])
        with open(f"letter_templates/letter_{num}.txt") as letter:
            letter = letter.read().replace("[NAME]", bday_df.iloc[idx]["name"])
        with smtplib.SMTP("smtp.gmail.com") as conn:  # and if not gmail, look for their server and replace
            conn.starttls()  # makes our connection secure
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(from_addr=EMAIL, to_addrs=bday_df.iloc[idx]["email"], msg=f"Subject:Happy Birthday!"
                                                                                    f"\n\n{letter}")
