import json
import os
from csv import DictReader, reader

#recommend having folks contract the ore to you from main in one hit.

def readFileDict(file="mining_ledger.txt", delimiter='\t'):
    records=[]
    with open(file, 'r') as csv_file:
        readfile = DictReader(csv_file, delimiter=delimiter)
        for line in readfile:
            records.append(line)
    return records

def readFileCSV(file="characters.txt", delimiter=','):
    chars = []
    reverse_main_dict = {}
    with open(file, 'r') as csv_file:
        readfile = reader(csv_file, delimiter=delimiter)
        for line in readfile:
            main = line[0]
            for char in line:
                reverse_main_dict[char.strip()] = main.strip()
    return reverse_main_dict


def mergeMiningLedgerMain(miningLedgerArray, charactersArray):
    char_totals = {}
    for miningLedger in miningLedgerArray:
        #group all ores by 
        pilot = miningLedger['Pilot']
        if pilot in charactersArray.keys():
            main = charactersArray[pilot]
        else:
            main = pilot
        if main in char_totals.keys():
            if miningLedger['Ore Type'] in char_totals[main].keys():
                char_totals[main][miningLedger['Ore Type']] += int(miningLedger['Quantity'])
            else:
                char_totals[main][miningLedger['Ore Type']] =int(miningLedger['Quantity'])
        else:
            char_totals[main] = { miningLedger['Ore Type']: int(miningLedger['Quantity'])}

    
    return char_totals

miningLedgerArray = readFileDict("mining_ledger.txt")
#assumption that the first character is the main.
characters = readFileCSV("characters.txt")
totals = mergeMiningLedgerMain(miningLedgerArray=miningLedgerArray, charactersArray=characters)
print(totals)
