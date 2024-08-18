from src.config import CONFIG

from src.app.callbacks import register_all_callbacks
from src.app import app

if __name__ == "__main__":
    register_all_callbacks(app)
    app.run(
        host=CONFIG.networking.host,
        port=CONFIG.networking.port
    )
