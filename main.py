from os import system  # Used for clearing terminal
import logging
import pyautogui
import time  # Used for timeouts


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

system("cls")
logging.info("Initializing Script\n")

Running = True
Harvesting = True
Selling = False

def REPO():

    logging.info("Repositioning\n")
    pyautogui.moveTo(225, 143, duration=1)
    pyautogui.dragTo(666, 666, duration=1)
    pyautogui.keyDown("down")
    time.sleep(2)
    pyautogui.keyUp("down")

def PLANT():

    logging.info("Planting\n")
    pyautogui.click(714, 492)   # Click Control Soil
    time.sleep(1)
    pyautogui.moveTo(465, 475, duration=1)   # Move to Corn
    pyautogui.mouseDown()   # Click and hold corn
    pyautogui.moveTo(714, 492, duration=1)   # Move to plant Control Corn
    pyautogui.moveTo(526, 680, duration=1)  # Move to plant First Soil
    pyautogui.moveTo(1047, 418, duration=1)  # Move to plant F-Last Soil
    pyautogui.moveTo(621, 729, duration=1)  # Move to plant Second Soil
    pyautogui.moveTo(1145, 465, duration=1)  # Move to plant S-Last Soil
    pyautogui.mouseUp() # Release corn

def GROW():
    logging.info("Sleeping for 5 minutes\n")
    time.sleep(300)

def HARVEST():
    logging.info("Harvesting\n")
    pyautogui.click(714, 492)   # Click Control Soil
    time.sleep(1)
    pyautogui.moveTo(543, 443, duration=1)   # Move to Syth
    pyautogui.mouseDown()   # Click and hold syth
    pyautogui.moveTo(714, 492, duration=1)   # Move to cut Control Corn
    pyautogui.moveTo(526, 680, duration=1)  # Move to cut First Soil
    pyautogui.moveTo(1047, 418, duration=1)  # Move to cut F-Last Soil
    pyautogui.moveTo(621, 729, duration=1)  # Move to cut Second Soil
    pyautogui.moveTo(1145, 465, duration=1)  # Move to cut S-Last Soil
    pyautogui.mouseUp() # Release Syth

def OPENSHOP():
    pyautogui.click(626, 897)   # Open 

def SELL():

    time.sleep(1)
    pyautogui.click(270, 404)   # Open first slot
    time.sleep(1)
    pyautogui.click(467, 245)   # Click on corn
    time.sleep(1)
    pyautogui.click(1265, 472)  # Click max money
    time.sleep(1)
    pyautogui.click(1347, 600)  # Click advert
    time.sleep(1)
    pyautogui.click(1211, 826)  # Put on sale
    time.sleep(1)
    pyautogui.moveTo(518, 427, duration=1)  # Move mouse for drag
    pyautogui.mouseDown()
    pyautogui.moveTo(219, 427, duration=1)
    pyautogui.mouseUp()

def PICKUP():

    time.sleep(1)
    pyautogui.click(270, 404)   # Open first slot
    time.sleep(1)
    pyautogui.click(170, 387)   # Redundency click for unsold items


# START SCRIPT

while Running:

    # REPO
    REPO()

    while Harvesting:

        # PLANT
        PLANT()

        # REPO
        REPO()

        # GROW
        GROW()

        # HARVEST
        HARVEST()

        break

    # OPEN SHOP
    OPENSHOP()

    while Selling:

        # SELL
        SELL()
    
    break