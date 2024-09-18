import smtplib

my_email = "hoseinvsc@gmail.com"
password = "hlapvqgvrehwsmas"
#hlap vqgv rehw smas

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                     to_addrs="kazem3d@gmail.com",
                       msg="Subject:Hello\n\n This message is sent automatically by python{smtp}")
connection.close
