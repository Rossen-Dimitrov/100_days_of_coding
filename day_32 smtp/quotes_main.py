import smtplib
import datetime as dt


def send_mail(message):
    my_email = "dimitrov.rosen@gmail.com"
    password = "nzzkyhbesmtkoibu"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="rosty_d@abv.bg",
                            msg=f"Daily Quotes\n\n{message}")


def get_day_of_week():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    return day_of_week


with open("quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    message = all_quotes.pop()
with open("quotes.txt", "w") as quotes:
    quotes.write("".join(all_quotes))

if get_day_of_week() == 3:
    send_mail(message)
