import psutil
import winsound
import time
from colorama import init, Back, Style

init()  # Inicializa a biblioteca colorama

previous_percent = -1  # Valor inicial da porcentagem da bateria

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    if percent != previous_percent:
        previous_percent = percent

        if percent < 12:
            print(Back.RED + f"Porcentagem da bateria: {percent}%" + Style.RESET_ALL)
            print("Bateria está crítica")
            if not battery.power_plugged:
                print("Apitando por 10 segundos")
                winsound.Beep(440, 10000)
        elif percent < 19:
            print(Back.YELLOW + f"Porcentagem da bateria: {percent}%" + Style.RESET_ALL)
            print("Bateria está baixa")
            if not battery.power_plugged:
                print("Apitando por 3 segundos")
                winsound.Beep(440, 3000)
        else:
            print(Back.GREEN + f"Porcentagem da bateria: {percent}%" + Style.RESET_ALL)

    time.sleep(1)
