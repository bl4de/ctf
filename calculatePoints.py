#!/usr/bin/python
# @author bl4de https://github.com/bl4de | https://ctftime.org/team/12769
#
# CTF event points -> CTFtime.org ranking points calculator
# Rating formula see: https://ctftime.org/rating-formula/
#
#
# Calculates team's points from CTF for CTFtime.org overall ranking
#


def calculate():
    rating = 0.0

    points_coef = float(team_points) / best_points
    place_coef = float(1) / team_place

    if points_coef > 0:
        rating = ((points_coef + place_coef) * weight) / (1/(1+(team_place/total_teams)))

    return rating

if __name__ == '__main__':

    team_place = int(raw_input("your team place in CTF: "))
    team_points = int(raw_input("earned CTF points: "))
    total_teams = int(raw_input("teams with any points (more than 0) in CTF: "))
    best_points = int(raw_input("winner team points: "))
    weight = int(raw_input("CTF event rating weight (by CTFtime.org): "))

    print "\n### Your team earned {0:.4f} points in this CTF, congrats! ###"\
        .format(calculate())
