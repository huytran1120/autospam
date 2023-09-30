import random
import time
import pyautogui as pg
wd =(' are the reason i am alive',' are priceless', ' are my world', ' are my angel')
time.sleep(8)
for i in range(100):
    ms = random.choice(wd)
    pg.write("you" + ms)
    pg.press('enter')