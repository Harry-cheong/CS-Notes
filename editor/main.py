import sys

from cmd import Command
from config import Config

# Config
config = Config()

# CLI 
cmd = Command("./bin", config)

if (args_count := len(sys.argv) < 2):
    # cmd.info()
    cmd.exec(["main.py", ""])
else:
    cmd.exec(sys.argv)