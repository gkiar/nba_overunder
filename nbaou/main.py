#!/usr/bin/env python

from argparse import ArgumentParser

from nbaou.startup import set_line, set_teams, set_draft, draft
from nbaou.reporting import standings


def main():
    desc = ("NBA Over-Under (pronounced N-B-Oww) - tool for running an "
            "Over-Under league on NBA team win-loss projections.")
    parser = ArgumentParser("nbaou", description=desc)

    htext = """nbaou has several distinct modes of operation:
  - set_line:  This will walk you through the teams in the league and allow you
               set the betting line for each in terms of total number of wins.
               Run this before drafting.
  - set_teams: This will let you set the participants of your draft.
  - set_draft: This will let you set the number of rounds and generate the draft
               order. If a draft order has been set another way, still run this
               command and then resort the resulting file.
  - draft:     This will let you draft teams.
  - standings: This will show you the current leaderboard of your league. You
               can also use this to project the best-, worst-, and expected-case
               outcomes of the remaining games in the league.
"""
    subparsers = parser.add_subparsers(dest="mode", help=htext)

    sub_set_line = subparsers.add_parser("set_line", description="")
    sub_set_line.set_defaults(func=set_line)

    sub_set_teams = subparsers.add_parser("set_teams", description="")
    sub_set_teams.set_defaults(func=set_teams)

    sub_set_draft = subparsers.add_parser("set_draft", description="")
    sub_set_draft.set_defaults(func=set_draft)

    sub_draft = subparsers.add_parser("draft", description="")
    sub_draft.set_defaults(func=draft)

    sub_standings = subparsers.add_parser("standings", description="")
    sub_standings.set_defaults(func=standings)

    inps = parser.parse_args()
    inps.func(**vars(inps))


if __name__ == "__main__":
    main()

