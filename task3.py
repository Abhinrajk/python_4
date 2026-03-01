#3. School Notification System (Polymorphism with Methods)

class Notification:
    def send_message(self):
        print("Sending a notification...")


class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email.")


class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS.")


class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via Mobile App.")


# Creating objects
notification1 = EmailNotification()
notification2 = SMSNotification()
notification3 = AppNotification()

# Demonstrating Polymorphism
notifications = [notification1, notification2, notification3]

for notify in notifications:
    notify.send_message()