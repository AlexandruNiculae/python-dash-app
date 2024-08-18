from app.config import CONFIG

from app.callbacks import register_all_callbacks
from app import app

if __name__ == "__main__":
    register_all_callbacks(app)
    app.run(
        host=CONFIG.networking.host,
        port=CONFIG.networking.port
    )
