# 🌹 The Hatchlor 🌹 Cookiecutter Template

The Hatchlor is a [cookiecutter] template featuring the modern and extensible Python project manager [hatch] 🐣.

## ✨ Features

The Hatchlor integrates the following features:

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
* [EditorConfig]: maintain consistent coding styles for multiple developers,
* [src-layout]: the actual Python package is kept under a `src` folder avoiding many common errors.

The template includes a `skeleton.py` with a simple function `fib` that calculates the Fibonacci numbers
as demonstration. This is tested with `tests/test_skeleton.py` to demonstrate the corresponding features
from above. As an additional tidbit, `skeleton.py` also features [Typer] to show how `fib` can be
exposed as a CLI command. These files are only for demonstration and can be safely deleted.

## 💫 Quickstart

Install the latest [cookiecutter], i.e. >= 1.4, if not installed:

```console
pip install -U cookiecutter
```

Then generate your Python project with:

```console
cookiecutter https://github.com/florianwilhelm/the-hatchlor.git
```

🎉 That's  it! You can now change into the created directory and check out `README.md` for more.

## 🪪 License

The Hatchlor is distributed under the terms of the [MIT license](LICENSE.txt).

## 🙏 Credits

To start this project off a lot of inspiration was taken from [cookiecutter-pypackage] and [Pyscaffold].

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
[black]: https://black.readthedocs.io/
[ruff]: https://beta.ruff.rs/
[EditorConfig]: http://editorconfig.org/
[Typer]: https://typer.tiangolo.com/
