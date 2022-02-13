import glob
from pathlib import Path
import logging
from . import Bot
from telethon_events import load_plugins

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "Spider-Man/Telethon/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")

if __name__ == "__main__":
    Bot.run_until_disconnected()