from .keygen import create_random_key
from .models import URL
from .schemas import ShortURL


async def get_db_url_by_key(url_key) -> URL:
    db_url = await URL.find_one({"url_key": url_key})
    return db_url


async def create_db_url(url: ShortURL) -> URL:
    if url.url_key is None or url.url_key == "":
        url.url_key = create_random_key(5)

    if (await get_db_url_by_key(url.url_key)).target_url != url.target_url:
        return None

    if db_url := await URL.find_one(URL.target_url==url.target_url):
        if url.url_key in db_url.url_key:
            return db_url
        db_url.url_key.append(url.url_key)
        await db_url.save()
        return db_url

    db_url = URL(
        target_url=url.target_url,
        url_key=[url.url_key]
    )
    await db_url.create()

    return db_url