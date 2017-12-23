#!/usr/bin/python3
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def __init__(self):
        host = "smtp.gmail.com"
        port = 587
        conn_email = SMTP(host, port)
        print(conn_email.ehlo())
        print(conn_email.starttls())

    def sendEmail(self):
        self.username = Gtk.Entry.get_text("username")
        self.password = Gtk.Entry.get_text("password")
        self.to_list = Gtk.Entry.get_text("to_list")
        self.message = Gtk.Entry.get_text("message")
        from_email = self.username

        try:
            self.conn_email.login(self.username, self.password)
            self.sendmail(from_email, self.to_list, self.message)
        except SMTPAuthenticationError:
            print("Could not login!")
        except:
            print("An error occured!")
        self.conn_email.quit()


    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)


builder = Gtk.Builder()
builder.add_from_file("design.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.set_title("Send Gmail")
window.show_all()

Gtk.main()
