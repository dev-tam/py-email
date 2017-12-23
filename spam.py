from smtplib import SMTP, SMTPAuthenticationError, SMTPException


host = "smtp.gmail.com"
port = 587
username = "jhon@example.com"
password = "wrongpass"
from_email = username
to_list = ["email1@example.com", "email2@example.com"]
message= "This is 2nd method"

conn_email = SMTP(host, port)
conn_email.ehlo()
conn_email.starttls()
try:
	conn_email.login(username, "wrongpass")
	conn_email.sendmail(from_email, to_list, message)	
except SMTPAuthenticationError:	
	print("Could not login!")
except:
	print("An error occured!")
conn_email.quit()