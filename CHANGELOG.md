# Changelog

## Version 0.6

- Fix: `PIP_COMPILE_UPGRADE_PACKAGE` instead of `PIP_COMPILE_UPGRADE` in `upgrade-pkg` hatch command
- Chg: Set `pip-compile-hashes = false` in `pyproject.toml`
- Chg: Add `"Programming Language :: Python :: 3.12"`
- Chg: Let the `lint` environment not inherit from default to avoid inconsistencies with pre-commit
- Upd: Bump version of ruff to 0.4.4 and mypy 1.10
- Chg: Lock file support is no longer experimental
- Add: Github Actions workflows

## Version 0.5

- Chg: remove note about adding `hatch config set dirs.env.virtual .direnv` as hatch is supported by VSC 1.88
- Fix: remove `license-files` from `pyproject.toml` as this is not standardized

## Version 0.4

- Chg: update `.pre-commit-config.yaml` to newest version
- Fix: remove `skip-install = true` in the `lint` environment which seems to have suppressed some mypy errors
- Fix: remove superfluous `exclude: '^docs/conf.py'` from `.pre-commit-config.yaml`
- Chg: Changed `pyproject.toml` according the new ruff configuration
- New: Activate social cards in mkdocs by default
- Chg: Updated hatch-pip-compile, ruff & mypy versions in `pyproject.toml`
- Fix: Some mkdocs deprecations, i.e. `materialx.emoji.twemoji`

## Version 0.3

- New: use `post-install-commands = ["pre-commit install"]` in `pyproject.toml` to make sure the pre-commit hook is installed
- Chg: have a clean `default` environment and test-related tools are now in `test` environment
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
