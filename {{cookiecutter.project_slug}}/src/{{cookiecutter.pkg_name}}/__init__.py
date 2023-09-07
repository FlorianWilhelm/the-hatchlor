"""Ultimate Notion provides a pythonic, high-level API for Notion

Notion-API: https://developers.notion.com/reference/intro
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('{{ cookiecutter.project_slug }}')
except PackageNotFoundError:  # pragma: no cover
    __version__ = 'unknown'
finally:
    del version, PackageNotFoundError
