#!/usr/bin/env python3
from requests import get
import sqlite3
from os.path import exists
import json

def create_user():
    db = sqlite3.connect("/opt/terraria/tshock/tshock.sqlite")
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE Username="superadmin";')
    if cursor.fetchall()[0][0] == 0:
        cursor.execute('INSERT INTO Users (Username, Password, Usergroup) VALUES ("superadmin", "$2a$07$S7i/jFGLQQzAItq0RlQJd.D4/npGbFwUGCZwe1QfqHRCDrYk0GxQK","superadmin");')
    cursor.close()
    db.commit()
    db.close()


def get_token():
    if exists("/tmp/clitoken"):
        with open("/tmp/clitoken", "r") as f:
            return f.read().strip()
    else:
        token = get("http://127.0.0.1:7878/token/create/superadmin/ballsack").json()["token"]
        with open("/tmp/clitoken", "w") as f:
            f.write(token)
        return token


def destroy_token(token):
    get("http://127.0.0.1:7878/token/destroy/"+token, params={"token":token})


def run_command(command, token):
    return get("http://127.0.0.1:7878/v2/server/rawcmd", params={"token":token, "cmd":command}).json()


def status():
    return get("http://127.0.0.1:7878/v2/server/status").json()


def main():
    import argparse

    parser = argparse.ArgumentParser("Terraria REST CLI")
    parser.add_argument("-a", "--action", help="action to take", choices=["mkuser", "cmd", "gettoken", "status"], required=True)
    parser.add_argument("-c", "--command", help="command to run")
    parser.add_argument("-t", "--token", help="api token, if needed")

    args = parser.parse_args()

    if args.action=="cmd":
        if not args.token:
            args.token = get_token()
        print(json.dumps(run_command(args.command, args.token), indent=4))
    elif args.action=="status":
        print(json.dumps(status(), indent=4))
    elif args.action=="gettoken":
        print(get_token())
    elif args.action=="deltoken":
        destroy_token(args.token)
    elif args.action=="mkuser":
        create_user()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
