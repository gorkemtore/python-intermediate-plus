import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "gorkemtore1@gmail.com"
PASSWORD = "--------"
# 1. Update the birthdays.csv
b_days_data = pandas.read_csv(filepath_or_buffer="birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
current_day = dt.datetime.now().day
current_month = dt.datetime.now().month
current_date = (current_month, current_day)

for data in b_days_data.iterrows():
    name = data[1]["name"]
    email = data[1]["email"]
    day = data[1]["day"]
    month = data[1]["month"]
    b_date = (month, day)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
    if current_date == b_date:
        filepath = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file=filepath) as letter_file:
            letter = letter_file.readlines()
            letter[0] = letter[0].replace("[NAME]", name)
            message = "Subject:Birthday Message\n\n"
            for row in letter:
                message += row
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="gorkemtore@yahoo.com",
                                msg=message)
        print("Email was sent")



