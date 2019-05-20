# auto_vultr_tool

auto manage vultr nodes. with vultr api and linux's crontab, we can auto create, destroy, start, stop node.

## Usage:

set vultr key to env

```
export VULTR_KEY=""
```

create, destroy, dump node

```
export PYTHONPATH=`pwd`
python tool.py create
python tool.py destroy
python tool.py dump
```

## dep

vultr refer from https://github.com/spry-group/python-vultr