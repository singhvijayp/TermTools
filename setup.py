import os, sys, time

time.sleep(2)
os.system("clear")
time.sleep(2)
print("\033[1;36mPlease Wait... Installing Requirements.")
time.sleep(3)
os.system("apt install python git -y")
time.sleep(2)
print(" ")
print("\033[0;0m Setup Finished. Launching the tool...")
time.sleep(2)
os.system("python termtools.py")
