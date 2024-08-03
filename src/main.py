from app import app
from app.callbacks import register_all_callbacks

if __name__ == "__main__":
    register_all_callbacks(app)
    app.run()
