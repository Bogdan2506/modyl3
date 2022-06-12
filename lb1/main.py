from flask import Flask

import random

### Make the flask app
app = Flask(__name__)

### Routes
@app.route('/')
def index():

    array = ["Bogdan", "Kovalskiy", "KID-21"]

    random_thing = random.randrange(len(array))

    if (array[random_thing]) == "Bogdan":
        return 'Hello, Bogdan'
    elif (array[random_thing]) == "Kovalskiy":
        return 'Kovalskiy its my surname'
    else:
        return 'KID-21 its my group'

### Start flask
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)