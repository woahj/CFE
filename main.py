from time import sleep
from Logger.Logger import Logger
from Config import Config
from Browser import Browser
import os


log = Logger().createLogger()
config = Config()
browser = Browser(log, config)

username = (os.environ.get('user'))
password = (os.environ.get('pass'))
if browser.login(username, password):
    log.info("Successfully logged in")
    while True:
        try:
            print("doing loop")
            browser.getLiveMatches()
            browser.cleanUpWatchlist()
            browser.startWatchingNewMatches()
            print("looped")
            log.debug(f"Currently watching: {', '.join([m.league for m in browser.liveMatches.values()])}")
            sleep(10)
        except KeyboardInterrupt:
            browser.stopMaintaininingSession()
            browser.stopWatchingAll()
            break
else:
    log.error("Login FAILED")
