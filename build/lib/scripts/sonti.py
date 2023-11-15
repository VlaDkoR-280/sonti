#!/usr/bin/python3
import argparse
from scripts import auth


from colorama import Fore, Style, init

def run():
	print("""
                            .:.
                          .-=+=:
                        .-=++++==:
                      .:=++++++++==:
                    .:=++++====++++=-.
                  .:=+++++=:  .:=++++=-.
                .:=++++==:      .-=++++=-.
               :=+++++=:          .-=++++=:.
               .-=++++=:
                 :-++++==:           .:.
                   :==+++=-.       .-=-.
                     :=++++=-.   .:=++-.
                      .:==++=: .:=++++-.
                        .:=+=: .::::::.
                          .-=:.
        :-======:          :=======:
         .:==+++=-:      .-=++++=-:
           .-=++++=-.  .-=++++==:
             .-=++++=--=++++==:
               .-=++++++++==:
                 :==+++++=:
                   :=++=:.
                     ::
  """)
	web_sites = 'Россия'	
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     usage="python3 sonti.py [search arguments...] nickname\n",
                                     description=f"{Fore.CYAN}\nСправка{Style.RESET_ALL}",
                                     epilog=(f"{Fore.CYAN}sonti {Style.BRIGHT}{Fore.RED}demo version {Style.RESET_ALL}" + \
                                             f"{Fore.CYAN}поддержка: \033[31;1mflagB\033[0m \033[36mWebsites!\n{Fore.CYAN}" + \
                                             f"Snoop \033[36;1mfull version\033[0m \033[36mподдержка: \033[36;1m{web_sites} \033[0m" + \
                                             f"\033[36mWebsites!!!\033[0m\n\n"))
	
	service_group = parser.add_argument_group('\033[36mservice arguments\033[0m')
	service_group.add_argument("--version", "-V", action="store_true", help="\033[36mA\033[0mbout: вывод на печать версий Sonti")
	service_group.add_argument("--start", "-s", action="store", help="\033[36mA\033[0mbout: Время и дата начала тегирования hh.mm.ss dd.mm.yyyy")	
	service_group.add_argument("--verbose", "-v", action="store_true", help="\033[36mA\033[0mbout: Вывод таблицы непосредственно в консоль")
	service_group.add_argument("--auth", action="store_true", help="\033[36mA\033[0mbout: Аутентификация в сессии...")


	#########################################################################################################


	search_group = parser.add_argument_group('\033[36msearch arguments\033[0m')
	search_group.add_argument("username", nargs='*', metavar='nickname', action="store", default=None,
                              help="\033[36mН\033[0mикнейм разыскиваемого пользователя, вводить с @ в начале. \
                                    Поддерживается поиск одновременно нескольких имен для этого вводить черз пробел."
                             )

	args = parser.parse_args()

	if args.version:print("Тебя волновать не должно, сопляк")	
	if args.auth:
		auth.Auth()
		print('Аутентификация прошла успешно!\nДля просмотра команд введите: sonti --help')
	start = args.start	
	usernames = args.username
	if (usernames):
		timeStart = ''
		dataStart = ''
		timeEnd = ''
		dataEnd = ''
		if (start):
			if (start.find(' ')):
				timeStart, dataStart = map(str, start.split())
			else:
				timeStart = start
		if args.verbose:
			print("\033[36mНикнейм     Имя       Время появления в сети   Дата появления в сети\033[0m")
			auth.watchOfUsers(usernames, True)
		else: auth.watchOfUsers(usernames, False)
