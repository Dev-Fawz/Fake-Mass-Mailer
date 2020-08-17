import time

# Create a fake list of a million email accounts

mailaccounts = list()
for count in range(1000000):
    mailaccounts.append(f"{count+1}@email.com")

# Using List Comprehension for the large size of email mailaccounts
send_gen = [print(f"Email sent to {mailaccounts}. ") for mailaccounts in mailaccounts]
#  Sending fake emails with a half a second wait delay
time.sleep(0.5)
