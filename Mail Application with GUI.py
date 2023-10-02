import smtplib
from tkinter import *

def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = to_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", END)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            email_text = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, recipient_email, email_text)
            status_label.config(text="Email sent successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

root = Tk()
root.title("Mail Application")

sender_email_label = Label(root, text="Sender Email:")
sender_email_label.pack()
sender_email_entry = Entry(root)
sender_email_entry.pack()

sender_password_label = Label(root, text="Sender Password:")
sender_password_label.pack()
sender_password_entry = Entry(root, show="*")
sender_password_entry.pack()

to_label = Label(root, text="To:")
to_label.pack()
to_entry = Entry(root)
to_entry.pack()

subject_label = Label(root, text="Subject:")
subject_label.pack()
subject_entry = Entry(root)
subject_entry.pack()

message_label = Label(root, text="Message:")
message_label.pack()
message_text = Text(root, height=5, width=30)
message_text.pack()

send_button = Button(root, text="Send Email", command=send_email)
send_button.pack()

status_label = Label(root, text="", fg="black")
status_label.pack()

root.mainloop()

