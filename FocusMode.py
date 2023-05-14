import time
import pyuac
import datetime
import ctypes
import sys


def main():
    current_time = datetime.datetime.now().strftime("%H:%M")
    Stop_time = input("Enter time example:- [10:10]:- ")
    a = current_time.replace(":", ".")
    a = float(a)
    b = Stop_time.replace(":", ".")
    b = float(b)
    Focus_Time = b-a
    Focus_Time = round(Focus_Time, 3)
    host_path = 'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'

    print(current_time)
    time.sleep(2)
    # Enter the websites that you want to block
    website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]
    if (current_time < Stop_time):
        with open(host_path, "r+") as file:  # r+ is writing+ reading
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
                    print("DONE")
                    time.sleep(1)
            print("FOCUS MODE TURNED ON !!!!")

    while True:

        current_time = datetime.datetime.now().strftime("%H:%M")
        # Enter the websites that you want to block
        website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]
        if (current_time >= Stop_time):
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()

                print("Websites are unblocked !!")
                file = open("focus.txt", "a")
                # Write a 0 in focus.txt before starting
                file.write(f",{Focus_Time}")
                file.close()
                break

if __name__ == "__main__":
    if not pyuac.isUserAdmin(): 
        pyuac.runAsAdmin()

    else:
        main()