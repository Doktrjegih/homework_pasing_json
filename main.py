import json
import csv


def add_book_to_json(book, data_to_json):
    data_to_json[counter]["books"].append(
        {
            "title": book["title"],
            "author": book["author"],
            "pages": book["pages"],
            "genre": book["genre"],
        }
    )


users = []
books = []
data_to_json = []

with open("users.json", "r", encoding="utf-8") as reader:
    data = json.load(reader)
    for user in range(len(data)):
        user_list = {
            "name": data[user]["name"],
            "gender": data[user]["gender"],
            "address": data[user]["address"],
            "age": data[user]["age"],
        }
        users.append(user_list)

with open("books.csv", "r", encoding="utf-8") as reader:
    data = csv.reader(reader, delimiter=",")
    next(data)
    for book in data:
        book_list = {
            "title": book[0],
            "author": book[1],
            "pages": book[3],
            "genre": book[2],
        }
        books.append(book_list)

while books:
    counter = 0
    for user, book in zip(users, books):
        generator = [user_["name"] for user_ in data_to_json]
        if user["name"] not in generator:
            data_to_json.append(
                {
                    "name": user["name"],
                    "gender": user["gender"],
                    "address": user["address"],
                    "age": user["age"],
                    "books": [],
                }
            )
        add_book_to_json(book, data_to_json)
        counter += 1
    for i in range(counter):
        books.pop(0)

with open("result.json", "w", encoding="utf-8") as writer:
    json.dump(data_to_json, writer, indent=4)
