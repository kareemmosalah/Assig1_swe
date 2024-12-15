from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from routes.books_routes import books_api

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(books_api, url_prefix='/api/books')

# Swagger UI
SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Library Management API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    print("Swagger UI available at http://localhost:8080/api-docs")
    app.run(debug=True, host="0.0.0.0", port=5000)