# Changelog

## Version 0.3

- New: use `post-install-commands = ["pre-commit install"]` in `pyproject.toml` to make sure the pre-commit hook is installed
- Change: have a clean `default` environment and test-related tools are now in `test` environment
- Change: set `path=.direnv` in `pyproject.toml` directly for VSCode support, instead of giving the hint to set it globally
- New: add [pytest-sugar](https://github.com/Teemu/pytest-sugar/) to `test` environment
- New: experimental lock-file support using [hatch-pip-compile](https://github.com/juftin/hatch-pip-compile)

## Version 0.2.3

- fix: license `proprietary` doesn't break hatch as it is no SPX license

## Version 0.2.2

- Fix: replace periods with underscores when determining `pkg_name` from `project_slug`
- Fix: add `[tool.hatch.build]` -> `packages` in `pyproject.toml` to resolve package if `project_slug` != `pkg_name`
- Fix: have less dependencies in the `pyproject.toml` as example to speed up demonstrations

## Version 0.2.1

- Fix: `CHANGELOG.md` in template included the changes of Hatchlor itself, now it's a dummy again

## Version 0.2

- New: allow the selection of Python 3.12 when setting up the template
- New: removed `black` as formatter as this is now done by `ruff format`
- New: commands in the `lint` environment state their version
- New: use the new `Annotated[...]` style for `typer` in `skeleton.py`
- Fix: have `pytest` omit `_version.py` as this file is generated on the fly by hatch-vcs
- Fix: let `ruff` also correct the files in `tests`, i.e. `include` configuration fixed
- Fix: removed unnecessary "fix requirements.txt" in `pre-commit` configuration
- Docs: more explanation of what `hatch` does and how to use it in `Readme.md` of the template
- Docs: more explanation of `hatch` in general in the-hatchlor's `Readme.md`
- Test: also have a Github CI/CD test and a demo repo of the instantiated template

## Version 0.1

- New: First release of The Hatchlor cookiecutter template
