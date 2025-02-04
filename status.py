from flask import Flask
from mcstatus import JavaServer, BedrockServer
app = Flask(__name__)

status = JavaServer.lookup('103.229.52.14:25910', timeout=2).status()
ping = status.latency
player = status.players

@app.route('/ping')
def ping():
    ping = ping
if __name__ == '__main__':
    app.run(debug=True, port=25910)
