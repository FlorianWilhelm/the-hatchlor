# 🌹 The Hatchlor 🌹 Cookiecutter Template

The Hatchlor is a [cookiecutter] template featuring the modern and extensible Python project manager [hatch] 🐣.

## ✨ Features

This template integrates the following features:

* [hatch]: Python packaging, environment management and test runner ([tox] replacement),
* [hatch-vcs]: determine the package version automatically from git tags, e.g. `v0.9`,
* [pytest]: full-featured Python testing tool that helps you write better programs,
* [coverage]: tool for measuring code coverage of Python programs with pytest integration,
* [ruff]: extremely fast Python linter, which replaces [isort], [flake8], etc.,
* [mypy]: optional static type checker for Python,
* [black]: the uncompromising Python code formatter everyone loves,
* [mkdocs]: a fast, simple and downright gorgeous static site generator,
* [pre-commit]: pre-commit git hooks that make your life easier,
* [Markdown]: instead of reStructuredText, Markdown is used consistently for all text files,
* [src-layout]: the actual Python package is kept under a `src` folder avoiding many common errors.

## 💫 Quickstart

Install the latest [cookiecutter], i.e. >= 1.4, if not installed:

```console
pip install -U cookiecutter
```

Then generate your Python project with:

```console
cookiecutter https://github.com/florianwilhelm/hatchlor.git
```

That's  it! 🎉 Now change into the created directory and checkout the `README.md` for more.

## 🪪 License

The Hatchlor is distributed under the terms of the [MIT license](LICENSE.txt).

## 💳 Credits

To start this project off a lot of inspiration and code was taken from [cookiecutter-pypackage] and [Pyscaffold].

[cookiecutter]: https://cookiecutter.readthedocs.io/
[tox]: https://tox.wiki/
[hatch]: https://hatch.pypa.io/
[hatch-vcs]: https://github.com/ofek/hatch-vcs
[cookiecutter-pypackage]: https://github.com/audreyfeldroy/cookiecutter-pypackage
[Pyscaffold]: https://pyscaffold.org/
[pre-commit]: https://pre-commit.com/
[mkdocs]: https://www.mkdocs.org/
[Markdown]: https://www.markdownguide.org/
[src-layout]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[flake8]: https://pypi.org/project/flake8/
[isort]: https://pycqa.github.io/isort/
[pytest]: https://docs.pytest.org/
[coverage]: https://coverage.readthedocs.io/
[mypy]: https://mypy-lang.org/
[black]: https://github.com/psf/black
[ruff]: https://beta.ruff.rs/
