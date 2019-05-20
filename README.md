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

## Shadowsock Process:

1. create vultr start script

```
# install docker server
curl https://get.docker.com/ | sh
systemctl start docker && systemctl enable docker

# start shadowsock server
docker run -d --restart=always -p 12222:12222 fanach/ssserver -p 12222 -k siwalove --workers 10

# registry bind wan ip an sub_domain by dnspod api
curl -X POST https://dnsapi.cn/Record.Ddns -d 'login_token=id,token&format=json&domain_id=7362650&record_id=374320494&record_line_id=10%3D0&sub_domain=gfw'
```

2. get vultr script id

3. use shadownsock client to fuck ...

## dep

vultr module refer from https://github.com/spry-group/python-vultr