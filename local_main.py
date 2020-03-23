from Simulator.dir_reader import DirReader
from Simulator.server import app
from Test.ep_simulator import ep_simulator
from pathlib import Path
from threading import Thread
import os


def start_ep_simulator():
    ep_simulator.run(debug=False, host='0.0.0.0', port=5050)


d = DirReader(Path(os.curdir + "/Test/files_from_SP/"), 1)
d.start()
Thread(target=start_ep_simulator).start()
app.run(debug=False, host='0.0.0.0', port=5000)
