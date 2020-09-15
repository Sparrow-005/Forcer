from os import system
from time import sleep
from .const import debug
from colorama import Fore
from builtins import input
from platform import system as platform


class Display(object):

    __is_color = None
    total_lines = None
    account_exists = None

    def __init__(self, username=None, passlist=None, is_color=None):
        self.delay = 1.5
        self.username = username
        self.passlist = passlist
        self.colors_disabled = True
        self.cls = 'cls' if platform() == 'Windows' else 'clear'

        if Display.__is_color == None:
            Display.__is_color = is_color

    def clear(self):
        if not debug or self.colors_disabled:
            system(self.cls)

            if self.colors_disabled and self.__is_color:
                self.colors_disabled = False
        else:
            print('\n\n')

    def stats(self, password, attempts, browsers, load=True):
        self.clear()
        complete = round((attempts/Display.total_lines) * 100, 4)
        account_exists = self.account_exists if self.account_exists != None else ''

        if self.__is_color:
            print('{0}[{1}-{0}] {2}Wordlist: {3}{4}{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, self.passlist, Fore.RESET
            ))

            print('{0}[{1}-{0}] {2}Username: {3}{4}{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, self.username.title(), Fore.RESET
            ))

            print('{0}[{1}-{0}] {2}Password: {3}{4}{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, password, Fore.RESET
            ))

            print('{0}[{1}-{0}] {2}Complete: {3}{4}%{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, complete, Fore.RESET
            ))

            print('{0}[{1}-{0}] {2}Attempts: {3}{4}{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, attempts, Fore.RESET
            ))

            print('{0}[{1}-{0}] {2}Browsers: {3}{4}{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, browsers, Fore.RESET
            ))

            print('{0}[{1}-{0}] {2}Exists: {3}{4}{5}'.format(
                Fore.WHITE, Fore.CYAN, Fore.RED, Fore.YELLOW, account_exists, Fore.RESET
            ))

        else:
            print(
                f'[-] Wordlist: {self.passlist}\n[-] Username: {self.username}\n[-] Password: {password}')

            print(
                f'Complete: {complete}\n[-] Attempts: {attempts}\n[-] Browsers: {browsers}\n[-] Exists: {account_exists}')

        if load:
            sleep(self.delay)

    def stats_found(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print('\n{0}[{1}!{0}] {2}Congrats! Password Found{3}'.format(
                Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
            ))

            print('{0}[{1}+{0}] {2}Username: {1}{3}{4}'.format(
                Fore.YELLOW, Fore.GREEN, Fore.WHITE, self.username.title(), Fore.RESET
            ))

            print('{0}[{1}+{0}] {2}Password: {1}{3}{4}'.format(
                Fore.YELLOW, Fore.GREEN, Fore.WHITE, password, Fore.RESET
            ))
        else:
            print('\n[*] Congrats! Password Found\n[+] Username: {}\n[+] Password: {}'.format(
                self.username.title(), password
            ))

        sleep(self.delay)

    def stats_not_found(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print('\n{0}[{1}!{0}] {2}Password Not Found{3}'.format(
                Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
            ))
        else:
            print('\n[*] Oops! Password Not Found')

        sleep(self.delay)

    def shutdown(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print('\n{0}[{1}!{0}] {1}Shutting Down {0}Forcer{1}...{2}'.format(
                Fore.YELLOW, Fore.RED, Fore.RESET
            ))
        else:
            print('\n[!] Shutting Down Forcer...')

        sleep(self.delay)

    def info(self, msg):
        self.clear()

        if self.__is_color:
            print('{0}[{1}i{0}] {2}{3}{4}'.format(
                Fore.YELLOW, Fore.CYAN, Fore.RED, msg, Fore.RESET
            ))
        else:
            print('[i] {}'.format(msg))

        sleep(2.5)

    def warning(self, msg):
        self.clear()

        if self.__is_color:
            print('{1}[{0}!{1}] {1}{2}{3}'.format(
                Fore.CYAN, Fore.YELLOW, Fore.RED, msg, Fore.RESET
            ))
        else:
            print('[!] {}'.format(msg))

        sleep(self.delay)

    def prompt(self, data):
        self.clear()

        if self.__is_color:
            return input('{0}[{1}?{0}] {2}{3}{4}'.format(
                Fore.YELLOW, Fore.CYAN, Fore.RED, data, Fore.RESET
            ))
        else:
            return input('[?] {}'.format(data))
   


