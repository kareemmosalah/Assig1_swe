from flask import Blueprint, jsonify, request
from controllers.books_controller import BooksController

books_api = Blueprint('books_api', __name__)
controller = BooksController()

@books_api.route('', methods=['GET'])
def list_books():
    return jsonify(controller.list_books())

@books_api.route('/search', methods=['GET'])
def search_books():
    query_params = request.args
    return jsonify(controller.search_books(query_params))

@books_api.route('', methods=['POST'])
def add_book():
    data = request.json
    return jsonify(controller.add_book(data))

@books_api.route('/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.json
    return jsonify(controller.update_book(isbn, data))

@books_api.route('/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    return jsonify(controller.delete_book(isbn))