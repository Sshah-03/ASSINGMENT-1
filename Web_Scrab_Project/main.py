import asyncio
import pandas as pd
import logging

from scraper import fetch_hackernews, fetch_reddit, fetch_products

logging.basicConfig(level=logging.INFO)

async def main():
    hn, reddit, products = await asyncio.gather(
        fetch_hackernews(),
        fetch_reddit(),
        fetch_products(),
    )

    combined = hn + reddit + products

    df = pd.DataFrame(combined)
    df.to_csv("output.csv", index=False)

    logging.info("Data exported to output.csv")

if __name__ == "__main__":
    asyncio.run(main())
