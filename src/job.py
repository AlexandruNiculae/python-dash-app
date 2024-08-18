import os
from datetime import datetime

from app.config import CONFIG


if __name__ == "__main__":
    dirpath = CONFIG.data.path
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)

    filename = f"{datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}.txt"
    filepath = os.path.join(dirpath, filename)
    with open(filepath, 'w') as fp:
        fp.write("bap")
