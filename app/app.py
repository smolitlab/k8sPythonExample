import socket
import os
import logging
import time
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')
hostname = socket.gethostname()
title = os.environ.get("TITLE", "Example App")  
colorenv = os.environ.get("BG_COLOR")
color = f"background-color:{colorenv};"

def logloop ():
    while True:
        logging.info("Loop log")
        time.sleep(30)

@app.route('/health')
def health_check():
    # Add your custom health check logic here
    if all_required_services_are_running():
        app.logger.debug("A health 200 message")
        return 'OK', 200
    else:
        app.logger.error("An error 500 message")
        return 'Service Unavailable', 500

# Example health check logic, replace it with your actual logic
def all_required_services_are_running():
    # Replace this with your logic to check the health of your services
    # For example, check if the required processes are running
    return True

@app.route("/")
def home():
    app.logger.info("An info message.")
    return render_template('index.html', title=title, hostname=hostname, color=color)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
    logloop()
    