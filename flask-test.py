from flask import Flask, render_template
import datetime
import gpiozero

app = Flask(__name__)



@app.route("/")


def door_status():
    #### need to come up with a way to check if the pin has already been set
    #if not door1:
    #try:
    #gpiozero.DigitalInputDevice(7).close()
    door1 = gpiozero.DigitalInputDevice(7,True,None)
    response = "The Value is " + str(door1.value)
    #except:
    #    response = "The Value is " + str(door1.value)
        
    templateData = {
        'title' : 'Door Status' + str(door1),
        'response' : response
        }

    return render_template('door.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
