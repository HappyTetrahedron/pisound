#!/usr/bin/env python

from flask import Flask
from optparse import OptionParser
import subprocess

config = {}

app = Flask(__name__)


@app.route("/play")
def handle_action():
    process = subprocess.run(
        "aplay {}".format(config['soundfile']),
        shell=True
    )
    return ""


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port', default='7333', type='int',
                      help="Port")
    parser.add_option('-H', '--host', dest='host', default='0.0.0.0', type='string',
                      help="Host")
    parser.add_option('-s', '--soundfile', dest='soundfile', default='notification.wav', type='string',
                      help="Host")
    (opts, args) = parser.parse_args()
    config['soundfile'] = opts.soundfile
    app.run(opts.host, opts.port)
