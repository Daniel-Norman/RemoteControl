from bottle import route, run
import os

@route('/space')
def index():
    cmd = """
    osascript -e 'tell application "System Events" to keystroke space'
    """
    os.system(cmd)

@route('/left')
def index():
    cmd = """
    osascript -e 'tell application "System Events" to key code 123'
    """
    os.system(cmd)

@route('/right')
def index():
    cmd = """
    osascript -e 'tell application "System Events" to key code 124'
    """
    os.system(cmd)


run(host='192.168.0.7', port=4717)
