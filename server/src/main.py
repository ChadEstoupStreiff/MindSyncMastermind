from Server import Server
import logging
import time
from GameManager import GameManager 


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        Server().start()
        while True:
            GameManager().tick()
            time.sleep(0.05)
    except KeyboardInterrupt:
        stopFlag = True
        print("Exiting program...")
    logging.critical("STOPED")