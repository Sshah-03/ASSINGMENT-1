import httpx
import asyncio
import logging
from tenacity import retry, stop_after_attempt, wait_fixed

from decorators import rate_limit, cached
from models import HackerNewsItem, RedditPost, Product

logging.basicConfig(level=logging.INFO)

# Retry decorator
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
@cached
@rate_limit(2)
async def fetch_json(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

async def fetch_hackernews():
    top_ids = await fetch_json(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    )
    tasks = []
    for story_id in top_ids[:5]:
        tasks.append(
            fetch_json(
                f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            )
        )
    results = await asyncio.gather(*tasks)

    validated = []
    for item in results:
        validated.append(HackerNewsItem(**item).model_dump())
    return validated

async def fetch_reddit():
    data = await fetch_json(
        "https://www.reddit.com/r/python/.json"
    )
    posts = data["data"]["children"][:5]
    validated = []
    for post in posts:
        validated.append(
            RedditPost(
                title=post["data"]["title"],
                url=post["data"]["url"],
                author=post["data"]["author"],
            ).model_dump()
        )
    return validated

async def fetch_products():
    data = await fetch_json(
        "https://fakestoreapi.com/products"
    )
    validated = []
    for item in data[:5]:
        validated.append(Product(**item).model_dump())
    return validated
