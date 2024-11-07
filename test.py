import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class booksData(BaseModel):
    id:int
    title: str
    author: str
    price: float
    isbn: str

Book =[]
@app.get("/books")
async def getBooks():
    return Book

@app.post("/create")
async def createBook(books:booksData):
    Book.append(books)
    return Book

@app.delete("/{id}")
async def deleteBook(id:int):
    for book in Book:
        if book.id == id:
            Book.remove(book)
            
    return Book


@app.put("/update/{id}")
async def updateBook(id:int , item:booksData):
    for books in Book:
        if books.id == id:
            books.title = item.title
            books.author = item.author
            
    return Book
    