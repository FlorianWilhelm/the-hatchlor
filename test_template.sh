
#!/bin/sh
set -x -e

PROJ_DIR='python-hatch-project'

cd ..
if [ -d "$PROJ_DIR" ]; then
  rm -rf "$PROJ_DIR"
fi

cookiecutter --no-input hatchlor 

cd $PROJ_DIR

hatch run cov
hatch run lint:all


