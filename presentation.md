# [uv](https://docs.astral.sh/uv/)

- Webiste: https://docs.astral.sh/uv/
- Install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Update uv version: `uv self update`

## Install python versions

`uv python`

`uv python install 3.13.1`

`uv python uninstall 3.13.1`


## Start new project

`uv init my-project`

## Add packages

`uv add httpx`

Add to specific group: `uv add pytest --group dev`

Remove: `uv remove pytest --group dev`

Sync the packages: `uv sync`

Important: sync the packages without a specific group: `uv sync --no-group dev`

Important: run without a specific group: `uv run --no-group dev -- uvicorn --host $HOST --port $PORT app.main:app`

Tree: `uv tree`

## Tool management

`uvx pycowsay "Hello World!"`

`uvx ruff check .`

## Scripts with packages

Don't need to install packages, just pass `--with <package>`
`uv run --with rich script.py`

More about this: https://docs.astral.sh/uv/guides/scripts/#running-scripts

## Features

https://docs.astral.sh/uv/getting-started/features/#features
