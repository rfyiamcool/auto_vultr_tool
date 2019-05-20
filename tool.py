#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import socket
import sys,os
from os import environ
from json import dumps

from vultr import Vultr, VultrError


# Looks for an environment variable named "VULTR_KEY"
API_KEY = environ.get('VULTR_KEY')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(funcName)s():%(lineno)d] %(message)s'
)
logging.getLogger("requests").setLevel(logging.WARNING)


def get_vultr():
    print API_KEY
    if API_KEY == "" or API_KEY is None:
        print "not found key"
        sys.exit(99)

    return Vultr(API_KEY)


# https://www.vultr.com/api/#server_create
def create():
    vultr = get_vultr()
    dcid = 22        # idc中心
    vpsplanid = 201  # 价格
    osid = 167       # centos 7
    vultr.server.create(dcid, vpsplanid, osid, params={
        "SSHKEYID": "59f18601ad762",
        "SCRIPTID": 498439,
    })


def show_server_list():
    vultr = get_vultr()
    server_list = vultr.server.list()
    for server_id in server_list:
        print serverID


def add_ssh_key():
    vultr = get_vultr()
    sk = open("~/.ssh/id_rsa.pub").read()
    vultr.sshkey.create(socket.gethostname(), sk)


def destroy():
    vultr = get_vultr()
    try:
        server_list = vultr.server.list()
    except VultrError as ex:
        logging.error('VultrError: %s', ex)

    for server_id in server_list:
        if server_list[server_id]['power_status'] == 'running':
            logging.info(server_list[server_id]['label'] + " will be gracefully shutdown.")
            vultr.server.destroy(server_id)


def dump_info():
    vultr = get_vultr()

    try:
        logging.info('Listing backups:\n%s', dumps(
            vultr.backup.list(), indent=2
        ))

        logging.info('Listing ISOs:\n%s', dumps(
            vultr.iso.list(), indent=2
        ))

        logging.info('Listing OSs:\n%s', dumps(
            vultr.os.list(), indent=2
        ))

        logging.info('Listing plans:\n%s', dumps(
            vultr.plans.list(), indent=2
        ))

        logging.info('Listing regions:\n%s', dumps(
            vultr.regions.list(), indent=2
        ))

        logging.info('Listing servers:\n%s', dumps(
            vultr.server.list(), indent=2
        ))

        logging.info('Listing snapshots:\n%s', dumps(
            vultr.snapshot.list(), indent=2
        ))

        logging.info('Listing SSH keys:\n%s', dumps(
            vultr.sshkey.list(), indent=2
        ))

        logging.info('Listing startup scripts:\n%s', dumps(
            vultr.startupscript.list(), indent=2
        ))
    except VultrError as ex:
        logging.error('VultrError: %s', ex)


def main():
    logging.info('URL: https://www.vultr.com/api/')
    dump_info()


if __name__ == "__main__":
    cmd = "dump"

    if len(sys.argv) > 1:
        cmd = sys.argv[1]
    else:
        print "input args"
        sys.exit(99)

    if cmd == "dump":
        dump_info()
    elif cmd == "create":
        create()
    elif cmd == "add_ssh_key":
        add_ssh_key()
    elif cmd == "destroy":
        destroy()
    else:
        print "input args"