import requests
from datetime import datetime
import smtplib

MY_LAT = 54.689461
MY_LONG = 25.279860

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
if time_now.hour >= sunset or time_now.hour <= sunrise:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff, long_diff = iss_latitude - MY_LAT, iss_longitude - MY_LONG
    if (5 > lat_diff > -5) and (5 > long_diff > -5):
        email = "sender@email.com"
        password = "app password"
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=email, password=password)
            conn.sendmail(from_addr=email, to_addrs="receiver@email.com", msg=f"Subject:ISS OVERHEAD!\n\n"
                                                                              f"The ISS is over you, "
                                                                              f"GO AND CHECK NOW!!")
