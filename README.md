## Part 11 Local Setup

1. `pip install poetry` (or safer, follow the instructions: https://python-poetry.org/docs/#installation)
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. active a virtual environment `poetry install`
4. active virtual environment `poetry shell`
5. [UNIX]: Run the FastAPI server via poetry with the bash script: `poetry run ./run.sh`
6. [WINDOWS]: Run the FastAPI server via poetry with the Python command: `poetry run python app/main.py`
7. Open http://localhost:8001/


## Links

Ce projet se base sur plusieurs technologies open-sources dont les documentations sont regroupées ici:

- [Pipenv](https://docs.pipenv.org/)
- [Docker](https://docs.docker.com/get-started/)
- [Hadolint](https://github.com/hadolint/hadolint#configure)
- Python
    * [pytest](https://docs.pytest.org/en/7.1.x/)
    * [fastapi](https://fastapi.tiangolo.com/)
    * [SQLalchemy](https://www.sqlalchemy.org/)
    * [alembic](https://alembic.sqlalchemy.org/en/latest/)
    *  [poetry] (https://python-poetry.org/docs/#installation)