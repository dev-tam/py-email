#!/usr/bin/python3
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def sendEmail(self, username, password, to_list, message):
        host = "smtp.gmail.com"
        port = 587
        self.username = username
        self.password = password
        from_email = username
        self.to_list = to_list
        self.message = message

        conn_email = SMTP(host, port)
        conn_email.ehlo()
        conn_email.starttls()
        try:
            conn_email.login(username, password)
            conn_email.sendmail(from_email, to_list, message)
        except SMTPAuthenticationError:
            print("Could not login!")

        except:
            print("An error occured!")
        conn_email.quit()


    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)


builder = Gtk.Builder()
builder.add_from_file("design.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()
