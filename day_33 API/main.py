import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 42.697708
MY_LONG = 23.321867


def iss_visible():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now > sunset or time_now < sunrise:
        return True


def send_mail(email_address):
    print("Mail sent")
    my_email = "dimitrov.rosen@gmail.com"
    password = "nzzkyhbesmtkoibu"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_address,
                            msg="Subject:ISS is coming\n\nISS will be over your head")


while True:
    time.sleep(600)
    if iss_visible() and is_night():
        send_mail("rosty_d@abv.bg")
    else:
        print("It is not right time")
