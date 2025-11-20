#!/usr/bin/env python

# Lojban gismu candidate score evaluation script
# Version 0.5

# Copyright 2014 Riley Martinez-Lynch, except where
# Copyright 2012 Arnt Richard Johansen.
# Distributed under the terms of the GPL v3.

# Usage:
#
#   python gismu_score.py -o scores.data uan rakan ekspekt esper predpologa mulud
#   python gismu_best.py < scores.data
#

import platform
import sys

from marshal import load

from gismu_utils import GismuMatcher

def main(scores, gismus):

    # print("Sorting scores...")
    scores.sort(key=lambda x: x[0], reverse=True)

    # print("")
    # print("10 first gismu candidates are:")
    # print("")
    for record in scores[:10]:
        ...
        # print(record)

    # print("")
    # print("Excluding candidates similar to existing gismu...")
    matcher = GismuMatcher(gismus)
    for (score, candidate, _) in scores:
        gismu = matcher.find_similar_gismu(candidate)
        if gismu == None:
            # print("The winner is....\n")
            # print(candidate.upper())
            # print("")
            break
        else:
            ...
            # print("Candidate '%s' too much like gismu '%s'." % (candidate, gismu))
    else:
        ...
        # print("No suitable candidates in top 10 scores.")

if __name__ == '__main__':

    gismu_path = 'gismu-list.txt'
    # print("Reading list of gismu... ")
    gismus = [line.strip() for line in open(gismu_path, 'r')]

    scores = load(sys.stdin)
    # print("Loading scores... ", scores)
    # print("%d scores loaded." % len(scores))

    main(scores, gismus)

