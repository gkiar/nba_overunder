#!/usr/bin/env python

import requests
import pandas
import json
import os.path as op
import os

from nbaou.utils import create_record, edit_record
from nbaou.utils import get_teams, get_standings
from nbaou.config import data_dir

def set_line(cache=False, *args, **kwargs):
    if not op.isdir(data_dir):
        os.system("mkdir -p {0}".format(data_dir))

    teams = get_teams(cache=cache)

    tkeys = [k for k in teams.keys()]
    prompt = [teams[k] for k in tkeys]

    linefile = op.join(data_dir, "line.json")
    if op.isfile(linefile):
        with open(linefile, 'r') as fhandle:
            linedata = json.loads(fhandle.read())

        record = linedata.values()
        record = edit_record(prompt, record, dtype=float)
    else:
        record = create_record(prompt, dtype=float)

    linedata = {k: r for k, r in zip(tkeys, record)}

    with open(linefile, 'w') as fhandle:
        fhandle.write(json.dumps(linedata, indent=2))

def set_teams(*args, **kwargs):
    pass


def set_draft(*args, **kwargs):
    pass


def draft(*args, **kwargs):
    pass

