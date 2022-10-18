from time import sleep
from Logger.Logger import Logger
from Browser import Browser
import os


log = Logger().createLogger()
browser = Browser(log, config)

usernamer = (os.environ.get('user'))
passworder = (os.environ.get('pass'))

if browser.login(usernamer, passworder):
    log.info("Successfully logged in")
    while True:
        try:
            browser.getLiveMatches()
            browser.cleanUpWatchlist()
            browser.startWatchingNewMatches()
            log.debug(f"Currently watching: {', '.join([m.league for m in browser.liveMatches.values()])}")
            sleep(60)
        except KeyboardInterrupt:
            browser.stopMaintaininingSession()
            browser.stopWatchingAll()
            break
else:
    log.error("Login FAILED")
