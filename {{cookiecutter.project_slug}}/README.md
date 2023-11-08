# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Features

* Feature 1
* Feature 2
* ...

## Development

After having cloned this repository:

1. install [hatch] globally with [pipx], i.e. `pipx install hatch`,
2. \[only once\] install `pre-commit` globall with `pipx install pre-commit`
3. \[only once\] run `pre-commit install` to install [pre-commit],

and then you are already set up to start hacking.

A special feature that makes hatch very different from other familiar tools is that you almost never
activate, or enter, an environment. Instead, you use `hatch run env_name:command` and the `default` environment
is assumed for a command if there is no colon found. Thus you must always define your environment in a declarative
way and hatch makes sure that the environment reflects your declaration by updating it whenever you issue
a `hatch run ...`. This helps with reproducability and avoids forgetting to specify dependencies since the
hatch workflow is to specify everything directly in [pyproject.toml](pyproject.toml). Only in rare cases, you
will use `hatch shell` to enter the `default` environment, which is similar to what you may know from other tools.

To get you started, use `hatch run cov` or `hatch run no-cov` to run the unitest with or without coverage reports,
respectively. Use `hatch run lint:all` to run all kinds of typing and linting checks. Try to automatically fix linting
problems with `hatch run lint:fix` and use `hatch run docs:serve` to build and serve your documentation.
You can also easily define your own environments and commands. Check out the environment setup of hatch
in [pyproject.toml](pyproject.toml) for more commands as well as the package, build and tool configuration.

## Credits

This package was created with [The Hatchlor] project template.

[The Hatchlor]: https://github.com/florianwilhelm/the-hatchlor
[pipx]: https://pypa.github.io/pipx/
[hatch]: https://hatch.pypa.io/
[pre-commit]: https://pre-commit.com/
