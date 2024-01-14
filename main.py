import time
import socket
from playsound import playsound
from win10toast import ToastNotifier
from os import system

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

toaster = ToastNotifier()
prev_status = False


while True:
    internet_status = check_internet()
    if internet_status != prev_status:
        system("cls")
        system("cls")
        system("cls")
        if internet_status:
            print("\x1b[1;34m"+"Usted se ha conectado a Internet.")
            print("")
            print("")
            print("\x1b[1;34m"+":'######:::'#######::'##::: ##:'########::'######::'########::::'###::::'########:::'#######::")
            print("\x1b[1;34m"+"'##... ##:'##.... ##: ###:: ##: ##.....::'##... ##:... ##..::::'## ##::: ##.... ##:'##.... ##:")
            print("\x1b[1;34m"+" ##:::..:: ##:::: ##: ####: ##: ##::::::: ##:::..::::: ##:::::'##:. ##:: ##:::: ##: ##:::: ##:")
            print("\x1b[1;34m"+" ##::::::: ##:::: ##: ## ## ##: ######::: ##:::::::::: ##::::'##:::. ##: ##:::: ##: ##:::: ##:")
            print("\x1b[1;34m"+" ##::::::: ##:::: ##: ##. ####: ##...:::: ##:::::::::: ##:::: #########: ##:::: ##: ##:::: ##:")
            print("\x1b[1;34m"+" ##::: ##: ##:::: ##: ##:. ###: ##::::::: ##::: ##:::: ##:::: ##.... ##: ##:::: ##: ##:::: ##:")
            print("\x1b[1;34m"+". ######::. #######:: ##::. ##: ########:. ######::::: ##:::: ##:::: ##: ########::. #######::")
            print("\x1b[1;34m"+":......::::.......:::..::::..::........:::......::::::..:::::..:::::..::........::::.......:::")

            toaster.show_toast("Conectado a Internet", "¡Estás conectado a Internet!")
            playsound('connected.mp3')
        else:
            print("\x1b[1;31m"+"Perdiste la conexión.")
            print("")
            print("\x1b[1;31m"+"'########::'########::'######:::'######:::'#######::'##::: ##:'########::'######::'########::::'###::::'########:::'#######::")
            print("\x1b[1;31m"+" ##.... ##: ##.....::'##... ##:'##... ##:'##.... ##: ###:: ##: ##.....::'##... ##:... ##..::::'## ##::: ##.... ##:'##.... ##:")
            print("\x1b[1;31m"+" ##:::: ##: ##::::::: ##:::..:: ##:::..:: ##:::: ##: ####: ##: ##::::::: ##:::..::::: ##:::::'##:. ##:: ##:::: ##: ##:::: ##:")
            print("\x1b[1;31m"+" ##:::: ##: ######:::. ######:: ##::::::: ##:::: ##: ## ## ##: ######::: ##:::::::::: ##::::'##:::. ##: ##:::: ##: ##:::: ##:")
            print("\x1b[1;31m"+" ##:::: ##: ##...:::::..... ##: ##::::::: ##:::: ##: ##. ####: ##...:::: ##:::::::::: ##:::: #########: ##:::: ##: ##:::: ##:")
            print("\x1b[1;31m"+" ##:::: ##: ##:::::::'##::: ##: ##::: ##: ##:::: ##: ##:. ###: ##::::::: ##::: ##:::: ##:::: ##.... ##: ##:::: ##: ##:::: ##:")
            print("\x1b[1;31m"+" ########:: ########:. ######::. ######::. #######:: ##::. ##: ########:. ######::::: ##:::: ##:::: ##: ########::. #######::")
            print("\x1b[1;31m"+"........:::........:::......::::......::::.......:::..::::..::........:::......::::::..:::::..:::::..::........::::.......:::")
            toaster.show_toast("Desconectado de Internet", "¡Se ha perdido la conexión a Internet!")
            playsound('disconnected.mp3')
    prev_status = internet_status
    time.sleep(5)  # Verifica el estado de la conexión cada 5 segundos
