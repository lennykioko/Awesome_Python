import time
from datetime import datetime as dt

file_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

website_list = [
    # 'accounts.google.com',
    # 'mail.google.com',
    # 'myaccount.google.com',
    # 'www.facebook.com',
    # 'business.facebook.com',
    # 'thepiratebay.org',
    # 'piratepiratepirate.com',
]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        # print("Working hours.....")
        with open(file_path, "r+") as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    
    else:
        # print("Fun hours.....")
        with open(file_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(120)
