# import smtplib

my_email = "kestercmu@gmail.com"
password = "Kz19961005!CMU"
recipient_email = "kesterzhou@gmail.com"

# # connection = smtplib.SMTP('smtp.gmail.com', 587)
# # connection.starttls()
# # connection.login(user=my_email,password=password)
# # connection.sendmail(from_addr=my_email,to_addrs=recipient_email, msg="Hello, this is a test.")
# # connection.close()
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=recipient_email,
#         msg="Subject:Hello\n\nThis is the body message of a test email."
#     )

import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Thursday Motivation\n\n{quote}"
        )