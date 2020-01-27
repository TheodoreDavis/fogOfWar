"""
The flask application package.
"""

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HOME NOOK CANTER HILL'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

import fogOfWar.views

