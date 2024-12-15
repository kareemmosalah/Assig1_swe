import json
import os

class BooksController:
    FILE_PATH = 'src/models/books.json'

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w') as file:
                json.dump([], file)

    def _read_data(self):
        with open(self.FILE_PATH, 'r') as file:
            return json.load(file)

    def _write_data(self, data):
        with open(self.FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)

    def list_books(self):
        return self._read_data()

    def search_books(self, query_params):
        books = self._read_data()
        filtered_books = [
            book for book in books if all(
                str(book.get(key, "")).lower() == str(value).lower() for key, value in query_params.items()
            )
        ]
        return filtered_books

    def add_book(self, data):
        books = self._read_data()
        if any(book['isbn'] == data['isbn'] for book in books):
            return {"error": "Book with this ISBN already exists."}, 400
        books.append(data)
        self._write_data(books)
        return {"message": "Book added successfully."}, 201

    def update_book(self, isbn, data):
        books = self._read_data()
        for book in books:
            if book["isbn"] == isbn:
                book.update(data)
                self._write_data(books)
                return {"message": "Book updated successfully."}, 200
        return {"error": "Book not found."}, 404

    def delete_book(self, isbn):
        books = self._read_data()
        books = [book for book in books if book["isbn"] != isbn]
        self._write_data(books)
        return {"message": "Book deleted successfully."}, 200