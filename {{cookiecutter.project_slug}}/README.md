# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Features

* ToDo

## Development

After having cloned this repository:

1. install [hatch] globally with [pipx], i.e. `pipx install hatch`,
2. \[only once\] install `pre-commit` globall with `pipx install pre-commit`
3. \[only once\] run `pre-commit install` to install [pre-commit],

and then you are already set up to start hacking. Use `hatch run cov` or `hatch run no-cov` to run
the unitest with or without coverage reports, respectively. Or use `hatch run lint:all` to run all
kinds of typing and linting checks and `hatch run docs:servce` to build and serve the documentation.
Also, check out the environment setup of hatch in [pyproject.toml](pyproject.toml) for more commands.

## Credits

This package was created with [Cookiecutter] and [The Hatchlor] project template.

[Cookiecutter]: https://cookiecutter.readthedocs.io/
[The Hatchlor]: https://github.com/florianwilhelm/the-hatchlor
[pipx]: https://pypa.github.io/pipx/
[hatch]: https://hatch.pypa.io/
[pre-commit]: https://pre-commit.com/
