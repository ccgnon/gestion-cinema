from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates

from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from app.schemas.film import FilmSearchResults, Film, FilmCreate
from app import deps
from app import crud


# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


app = FastAPI(title="Film API", openapi_url="/openapi.json")

api_router = APIRouter()


# Updated to serve a Jinja2 template
# https://www.starlette.io/templates/
# https://jinja.palletsprojects.com/en/3.0.x/templates/#synopsis
@api_router.get("/", status_code=200)
def root(
    request: Request,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Root GET
    """
    films = crud.film.get_multi(db=db, limit=10)
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "films": films},
    )


@api_router.get("/film/{film_id}", status_code=200, response_model=Film)
def fetch_film(
    *,
    film_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single film by ID
    """
    result = crud.film.get(db=db, id=film_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Film with ID {film_id} not found"
        )

    return result


@api_router.get("/search/", status_code=200, response_model=FilmSearchResults)
def search_films(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="foudre"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for films based on label keyword
    """
    films = crud.film.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": films}

    results = filter(lambda film: keyword.lower() in film.label.lower(), films)
    return {"results": list(results)[:max_results]}


@api_router.post("/film/", status_code=201, response_model=Film)
def create_film(
    *, film_in: FilmCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new film in the database.
    """
    film = crud.film.create(db=db, obj_in=film_in)

    return film


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
