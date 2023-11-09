# Changelog

## Version 0.2.2

- Fix: replace periods with underscores when determining `pkg_name` from `project_slug`
- Fix: add `[tool.hatch.build]` -> `packages` in `pyproject.toml` to resolve package if `project_slug` != `pkg_name`

## Version 0.2.1

- Fix: `CHANGELOG.md` in template included the changes of Hatchlor itself, now it's a dummy again

## Version 0.2

- New: Allow the selection of Python 3.12 when setting up the template
- New: Removed `black` as formatter as this is now done by `ruff format`
- New: Commands in the `lint` environment state their version
- New: Use the new `Annotated[...]` style for `typer` in `skeleton.py`
- Fix: Have `pytest` omit `_version.py` as this file is generated on the fly by hatch-vcs
- Fix: Let `ruff` also correct the files in `tests`, i.e. `include` configuration fixed
- Fix: Removed unnecessary "fix requirements.txt" in `pre-commit` configuration
- Docs: More explanation of what `hatch` does and how to use it in `Readme.md` of the template
- Docs: More explanation of `hatch` in general in the-hatchlor's `Readme.md`
- Test: Also have a Github CI/CD test and a demo repo of the instantiated template

## Version 0.1

- New: First release of The Hatchlor cookiecutter template
