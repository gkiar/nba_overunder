#!/usr/bin/env python

import requests
import json
import os.path as op
import os

from nbaou.config import data_dir, year

def _get_misc_data(filename, url, cache=True):
    if not (op.isfile(filename) and cache):
        data = requests.get(url).json()
        with open(filename, 'w') as fhandle:
            fhandle.write(json.dumps(data, indent=2))


def get_standings(cache=False):
    standings_file = op.join(data_dir, "standings.json")
    url = "http://data.nba.net/prod/v1/current/standings_all.json"

    _get_misc_data(standings_file, url, cache)

    with open(standings_file, 'r') as fhandle:
        data = json.loads(fhandle.read())

    data = data["league"]["standard"]["teams"]
    keys = ["win", "loss"]
    standings = {f["teamId"]: (f[k] for k in keys)
                 for f in data}
    return standings


def get_teams(cache=False, year=year):
    teams_file = op.join(data_dir, "teams.json")
    url = "http://data.nba.net/prod/v1/{0}/teams.json".format(year)

    _get_misc_data(teams_file, url, cache)

    with open(teams_file, 'r') as fhandle:
        data = json.loads(fhandle.read())

    data = data["league"]["standard"]
    teams = {t["teamId"]: t["fullName"]
             for t in data
             if t["isNBAFranchise"]}
    return teams


def create_record(prompt, dtype=float):
    record = []
    for p in prompt:
        while True:
            newval = input("{0}: ".format(p))
            try:
                record += [dtype(newval)]
                break
            except:
                print("Please try again with input of type {0}".format(dtype))
    return record


def edit_record(prompt, record, dtype=float):
    for idx, (p, r) in enumerate(zip(prompt, record)):
        while True:
            newval = input("{0} ({1}): ".format(p, r))
            if newval == '':
                break
            try:
                record[idx] = dtype(newval)
                break
            except:
                print("Please try again with input of type {0}".format(dtype))
    return record
