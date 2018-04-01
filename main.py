#!/usr/bin/python

import sys
import csv
from collections import defaultdict
from pprint import pprint

from hierarchical import HierarchicalData

#import pandas as pd

data = "data/r16"

txt = data + "txt.csv"
blb = data + "blb.csv"

print "Reading data from files %s and %s" % (txt, blb)

#accounts = HierarchicalData()


def split_account_number(number_str):
    return [number_str[i:i+2] for i in range(0,12,2)]

def tree(): return defaultdict(tree)

def dicts(t): return {k: dicts(t[k]) for k in t}

def print_accounts(accounts):
    pass
    
accounts = tree()
accounts_simple = {}

with open(txt, "rb") as txt_file:
    txt_reader = csv.DictReader(txt_file, fieldnames=("account", "description"), delimiter=";")
    for row in txt_reader:
        #print row["account"], row["description"]
        this_account = split_account_number(row["account"])
        accounts[this_account[0]][this_account[1]][this_account[2]][this_account[3]][this_account[4]][this_account[5]]["descr"] = row["description"]
        accounts_simple[this_account[0]][this_account[1]][this_account[2]][this_account[3]][this_account[4]][this_account[5]]["descr"] = row["description"]
        
with open(blb, "rb") as blb_file:
    blb_reader = csv.DictReader(blb_file, fieldnames=("account", "budget", "spent"), delimiter=";")
    for row in blb_reader:
        this_account = split_account_number(row["account"])
        accounts[this_account[0]][this_account[1]][this_account[2]][this_account[3]][this_account[4]][this_account[5]]["budget"] = row["budget"]
        accounts[this_account[0]][this_account[1]][this_account[2]][this_account[3]][this_account[4]][this_account[5]]["spent"] = row["spent"]
        
#pprint(dicts(accounts))
print accounts