with open('emails.txt', 'r') as emails:
    email_list = emails.readlines()

print("The following are att emails:")

for email in email_list:
    if "att" in email:
        print(email.rstrip())