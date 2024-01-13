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
            print("Usted se ha conectado a Internet.")
            print("")
            print("")
            print("               xxxxxxxxxxxxxxxxxxxx")
            print("           xxxxx                   xxxx")
            print("         xxxxxxxxxxx                   xxx")
            print("       xxxxx            xxx              xx")
            print("      xxx    xxx          xxx              x")
            print("    xxx     xx              x               x")
            print("   xx      xx               x                x")
            print("   x       x              xx                 xx")
            print("  x        xx            xx                   xx")
            print("  x         xxxxx        x                     xx")
            print(" x              xxxx    xx                      x")
            print(" x                  xx  x   xxxx                xx")
            print("xx                   x  x      x                 x")
            print("x                    xx x                         x")
            print("x                    xx xxxxxx      x             x")
            print("x                  xx        xxxx   x             x")
            print("x                 xx            xx                x")
            print("x               xxx              x                x")
            print("x              xx                xx               x")
            print("x              x                  x               x")
            print("xx             xx                 xx             x")
            print(" xx             xxx                x             x")
            print("  xx              xx               x             x")
            print("    xx             xxxx            x            x")
            print("      xxx             xxxx         x           xx")
            print("        xxxx             xxxxx     x          xx")
            print("           xxxxx             xxxxx x       xxxx")
            print("               xxxxxx            xx     xxxx")
            print("                     xxxxxxxxxxxxxxxxxxx")

            toaster.show_toast("Conectado a Internet", "¡Estás conectado a Internet!")
            playsound('connected.mp3')
        else:
            print("Perdiste la conexión.")
            print("")
            print("                                 x       x              xx")
            print("                                  x      x             x")
            print("                        x          x     x          x")
            print("                        xxx        xx    x        x")
            print("                          xx             x       x         x x xx")
            print("                                                       xx")
            print("")
            print("")
            print("")
            print("                                                    xxxxxx")
            print("                             xxxxx                 xx    xxxxxxxx           xxx")
            print("                       xxxxx x   x                xx        xx  xxx         xxx")
            print("                    xxx    xx    x               xx               xx      xxxx")
            print("                  xxx            xxxxxxxxx       x                 x   xxxxxx")
            print("                  x   xx    x    x               x    xxxx         xxxxxxx")
            print("     xxxxxxxxxxxxxx   x     x    x               x            xx   xxxxx")
            print("   xxxxxxxxxxxxxxxx   x          x               x             x   x")
            print("xxxxx             xx        x    xxxxxxxxx       x     xxxx   xx   x")
            print("xxx                xxxxx         xx              x            x    x")
            print(" x                     xxxxxxx   x               xx           x   xx")
            print("                             xx  x                xx         xx xx")
            print("                              xxxx                  xxxxxxxxxx")
            print("")
            print("")
            print("                               xx     x")
            print("                            x x       x         xxx")
            print("                       xx x                x         x   x")
            print("                                     x      x               x  xx")
            print("                                     x      x")
            print("                                             x")
            print("                                     x       x")
            print("                                     x")
            print("                                     x")
            toaster.show_toast("Desconectado de Internet", "¡Se ha perdido la conexión a Internet!")
            playsound('disconnected.mp3')
    prev_status = internet_status
    time.sleep(5)  # Verifica el estado de la conexión cada 5 segundos
