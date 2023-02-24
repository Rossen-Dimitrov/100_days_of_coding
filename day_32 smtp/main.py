import smtplib
import datetime as dt
import pandas
import random
import os

birthdays = pandas.read_csv("birthdays.csv")


def send_mail(email_address, message):
    my_email = "dimitrov.rosen@gmail.com"
    password = "nzzkyhbesmtkoibu"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_address,
                            msg=f"Subject:Happy Birthday\n\n{message}")


today_birthday = {}

now = dt.datetime.now()
cur_month = now.month
cur_day = now.day

for record in birthdays.iterrows():
    month = record[1][3]
    day = record[1][4]
    name = record[1][0]
    email = record[1][1]
    if month == cur_month and day == cur_day:
        today_birthday[name] = email

directory_path = './letter_templates/'

if today_birthday:
    for person, email in today_birthday.items():
        random_file = f"./letter_templates/letter_{random.randint(1, len(os.listdir(directory_path)))}.txt"
        with open(random_file) as file:
            letter = file.read()
            letter = letter.replace("[NAME]", person)
            send_mail(email, letter)
