from time import sleep
from Logger.Logger import Logger
from Config import Config
from Browser import Browser
from boto.s3.connection import S3Connection


log = Logger().createLogger()
config = Config()
browser = Browser(log, config)

user = S3Connection(os.environ['user']
passw = S3Connection(os.environ['pass']

#is it obvious i dont know how to code
if browser.login(user, passw):
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
