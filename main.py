# [ REP 2K Time Clock Automation System ]

import os
import pyautogui as pa
import time
os.system("cls")
print('====================================================\n')

rep2k = input("Complete o Ip do REP2000 [172.16.????]")
# [Configurando input]
# Formato desejado : "172.16.90.45"
rep2k_str = str(rep2k)
rep2k = f"{'172.16.'}{rep2k_str[:2]}.{rep2k_str[2:]}"

print(rep2k)

"""
pa.press('win')
time.sleep(1)
pa.write("edge")
pa.press('enter')
time.sleep(5)
pa.keyDown('win')
pa.press('up')
pa.keyUp('win')
pa.PAUSE
pa.write("edge://settings/defaultbrowser")
pa.press('enter')
time.sleep(3)

pa.write("compatibilidade")
time.sleep(1)
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('enter')

#pa.write("http://192.168.0.1")
pa.write("http://")
pa.write(rep2k)
time.sleep(3)
pa.press('tab')
pa.press('enter')
"""