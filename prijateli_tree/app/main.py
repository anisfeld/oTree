import glob
import json
import os
from typing import Annotated, List

from fastapi import FastAPI, Header, Response
from fastapi.responses import JSONResponse
from fastapi_localization import TranslateJsonResponse

from prijateli_tree.app.config import config
from prijateli_tree.app.database import Base, engine
from prijateli_tree.app.routers import administration, games
from prijateli_tree.app.schemas import LanguageTranslatableSchema
from fastapi.staticfiles import StaticFiles
from prijateli_tree.app.utils.constants import (
    FILE_MODE_READ,
    KEY_ENV,
    LANGUAGE_ALBANIAN,
    LANGUAGE_ENGLISH,
    LANGUAGE_MACEDONIAN,
    LANGUAGE_TURKISH,
    STANDARD_ENCODING,
)


Base.metadata.create_all(bind=engine)

config = config[os.getenv(KEY_ENV)]

app = FastAPI(debug=config.DEBUG)

app.mount("/static", StaticFiles(directory="static"), name="static")

languages = {}
for lang in glob.glob("languages/*.json"):
    lang_code = lang.split("\\")[1].split(".")[0]

    with open(lang, FILE_MODE_READ, encoding=STANDARD_ENCODING) as file:
        languages[lang_code] = json.load(file)

app.include_router(
    administration.router,
    prefix="/admin",
    tags=["admin"],
)
app.include_router(
    games.router,
    prefix="/games",
    tags=["games"],
)


@app.post(
    "/language",
    response_class=TranslateJsonResponse,
    response_model=List[LanguageTranslatableSchema],
)
def set_language(accept_language: Annotated[str | None, Header()] = None) -> Response:
    if accept_language in [
        LANGUAGE_ENGLISH,
        LANGUAGE_TURKISH,
        LANGUAGE_MACEDONIAN,
        LANGUAGE_ALBANIAN,
    ]:
        config.LANGUAGE = accept_language
    else:
        config.LANGUAGE = LANGUAGE_ENGLISH

    return JSONResponse(content={"message": "It done worked"})


@app.get("/")
def funky():
    return {"Hello": "World"}
