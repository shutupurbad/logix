# BIN GENERATOR
import random
import time
import os

savefile = open(f"{os.getcwd()}\\saved.txt", 'a')

x = input("How much CC bins do you want generated?\n")
y = input("Do you want them to be in a file or not? y/n lowercase\n")

x = int(x)

print("CC BIN Generator by Logix#4224 on discord :)")
time.sleep(1)
print("Generating")
time.sleep(2)
for i in range(x):
    printed = random.randint(410000,520000)
    cwd = os.getcwd()
    print(printed)
    if y == "y":
        printed = str(printed)
        printed = printed + "\n"
        savefile.write(printed)
        savefile.flush()
input("Press Enter key to stop the application")
