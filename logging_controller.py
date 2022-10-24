import sys
from pathlib import Path
import datetime

class Logger:

    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')

    def write(self, message):
        self.console.write(message)
        self.file.write(message)

    def flush(self):
        self.console.flush()
        self.file.flush()

path = f'log/log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
(Path(path) / "..").mkdir(parents=True, exist_ok=True)
sys.stdout = Logger(path)
