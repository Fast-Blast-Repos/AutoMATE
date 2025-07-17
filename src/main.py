# Log
from utils.logger import log
import datetime
import os
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_dir = os.path.expanduser("data/logs")
os.makedirs(log_dir, exist_ok=True)  # Make sure log dir exists.
log_path = os.path.join(log_dir, f"{timestamp}.log")
log("Log file initialized...", log_path, 1)

# Colors
from utils import colors

# Parser
import argparse

parser = argparse.ArgumentParser(
                    prog='AutoMATE',
                    description='Automating stuff made easy.',
                    epilog='https://github.com/Fast-Blast-Repos/AutoMATE')

parser.add_argument('-d', '--dev', action='store_true') # Developer mode.
parser.add_argument('-C', '--clear_log', action='store_true') # Clear log function.

args = parser.parse_args()

# Clear logs if asked to.
if args.clear_log:
    if input(f"{colors.MAGENTA}Are you sure? [Y/n] {colors.OFF}").lower() != "n":
        for filename in os.listdir(log_dir):
            file_path = os.path.join(log_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{colors.BLUE}{filename}{colors.OFF} was removed.")
        print(f"{colors.GREEN}All logs removed successfully.{colors.OFF}")
        exit(0)
    else:
        print(f"{colors.YELLOW}Canceling...{colors.OFF}")
        exit(0)

devmode = args.dev

# Developer mode configuration.
if devmode:
    log("Running in developer mode...", log_path)
    CONFIG_PATH = "../configs"
else:
    CONFIG_PATH = "~/.config/AutoMATE"

# Configuration file parser.
from utils import config_parser as cfgprs
try:
    config = cfgprs.parse_config(CONFIG_PATH + "/config.json")
except Exception as e:
    log(f"Program exited during config load due to: {e}", log_path, 3)
    exit(1)
log("Successfully loaded configuration file...", log_path, 1)
