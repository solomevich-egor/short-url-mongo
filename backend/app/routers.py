from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

from .crud import create_db_url, get_db_url_by_key
from .models import URL
from .schemas import CreateShortURL, ShortURL

router = APIRouter(prefix="/short-url")


def get_url_info(db_url: URL):
    short_url_keys = []
    for key in db_url.url_key:
        print(key)
        short_url_keys.append(key)
    return ShortURL(
        target_url=db_url.target_url,
        url_key=short_url_keys
    )


@router.post("/url", response_model=ShortURL)
async def create_url(url: CreateShortURL):
    if db_url := await create_db_url(url):
        return get_url_info(db_url)
    else:
        raise HTTPException(status_code=404, detail="Passed url_key is already used")


@router.get("/{url_key}")
async def forward_to_target_url(
    url_key: str,
    request: Request
):
    if db_url := await get_db_url_by_key(url_key):
        return RedirectResponse(db_url.target_url)
    else:
        raise HTTPException(status_code=404, detail=request)
