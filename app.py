from flask import Flask, send_from_directory
import logging

def create_app() -> Flask:
    app = Flask(__name__)

    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("Starting Library Management System API")

    # Register blueprints
    from routes.auth import bp as auth_bp
    from routes.books import bp as books_bp
    from routes.members import bp as members_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(members_bp)

    # Serve frontend
    @app.route('/')
    def index():
        return send_from_directory('static', 'index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)