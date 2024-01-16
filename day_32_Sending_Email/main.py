import smtplib


my_email = "andreeabuciumanu1010@gmail.com"
my_password = ""
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="serban.robu@gmail.com", msg="Hello, baby!")
connection.close()

