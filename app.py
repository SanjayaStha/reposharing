from flask import Flask,render_template
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO 
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://fbb742719a5a48558af5fb6895e96522@o435044.ingest.sentry.io/5392824",
    integrations=[FlaskIntegration()]
)

app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():   
    return render_template("index.html")

@app.route('/hello')
def hello():   
    return render_template("hello.html")


@socketio.on('my_event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    socketio.run(app,debug =True)