from pydantic import BaseModel

class HackerNewsItem(BaseModel):
    title: str | None = None
    url: str | None = None
    by: str | None = None

class RedditPost(BaseModel):
    title: str
    url: str
    author: str

class Product(BaseModel):
    title: str
    price: float
    category: str
