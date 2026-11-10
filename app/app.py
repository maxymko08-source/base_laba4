import os
import yaml
from flask import Flask
from my_project import init_app


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_app() -> Flask:
    app = Flask(__name__)

    config_path = os.path.join(os.path.dirname(__file__), "config", "app.yml")
    cfg = load_config(config_path)

    db_cfg = cfg["database"]
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{db_cfg['user']}:{db_cfg['password']}"
        f"@{db_cfg['host']}:{db_cfg['port']}/{db_cfg['name']}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = cfg["flask"].get("secret_key", "dev-secret")

    init_app(app)
    return app, cfg


if __name__ == "__main__":
    application, cfg = create_app()
    flask_cfg = cfg.get("flask", {})
    application.run(
        host=flask_cfg.get("host", "0.0.0.0"),
        port=flask_cfg.get("port", 5000),
        debug=flask_cfg.get("debug", True),
    )
