from smtplib import SMTP

host = "smtp.gmail.com"
port = 587
username = "jhon@example.com"
password = "wrongpass"
from_email = username
to_list = ["email1@example.com", "email2@example.com"]


ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "This is 2nd method")
ABC.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
	pass_wrong.login(username, "wrongpass")
	pass_wrong.sendmail(from_email, to_list, "This is 2nd method")	
except SMTPAuthenticationError:	
	print("Could not login!")
except:
	print("An error occured")
pass_wrong.quit()