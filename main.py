import os
import shutil
login = "Self"
while True:
    current_login = os.getlogin()

    if current_login != login:
        print("Get trolled R.I.P your ram though")
        shutil.copyfile('main.py', 'main_duplicate.py')
#Created by Trebor-Sehguh
