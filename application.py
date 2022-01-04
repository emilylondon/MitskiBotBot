from flask import Flask
from tweet import mitski_reply
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

application = Flask(__name__)

@application.route("/")
def index():
    return "running the bot!"

def tweet():
    mitski_reply()
    print("Tweet successful")

scheduler = BackgroundScheduler()
scheduler.add_job(func=tweet, trigger="interval", hours=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    application.run(port=5000, debug=True)

