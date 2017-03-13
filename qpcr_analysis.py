#!/usr/bin/python
#this script analyze qpcr result automatically
#usage: python qpcr_analysis.py dirname
#eaample: python qpcr_analysis.py NPB_meta.tsv ermb.plate1 ermb.plate2 ermb.plate3 ermb.plate4 > ermb.qpcr.tsv

import sys
import glob

def make_full_table(meta,plate1,plate2,plate3,plate4):
    d = {}
    result = []
    for ids, item in meta.items():
        #print item
        result = item
        if item[0] == 'plate_1':
            item.append(plate1[item[1]][5])
            item.append(plate1[item[1]][6])
        elif item[0] == 'plate_2':
            item.append(plate2[item[1]][5])
            item.append(plate2[item[1]][6])
        elif item[0] == 'plate_3':
            item.append(plate3[item[1]][5])
            item.append(plate3[item[1]][6])
        elif item[0] == 'plate_4':
            item.append(plate4[item[1]][5])
            item.append(plate4[item[1]][6])
        #print result
        d[ids] = result
    return d

def read_meta(file):
    d = {}
    for line in open(sys.argv[1],'r'):
        spl = line.strip().split('\t')
        d[spl[0]+spl[1]] = spl
    return d

def read_summary(dir):
    d = {}
    path = dir + "/*Quantification*Summary*.txt"
    
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for line in f:
                spl = line.strip().split('\t')
                d[spl[0]]=spl

    return d

def main():
    #read meta
    meta = read_meta(sys.argv[1])
    
    #read file
    plate1 = read_summary(sys.argv[2])
    plate2 = read_summary(sys.argv[3])
    plate3 = read_summary(sys.argv[4])
    plate4 = read_summary(sys.argv[5])

    #make full table: merge meta and each plate
    full_table = make_full_table(meta,plate1,plate2,plate3,plate4)
    for ids, item in full_table.items():
        print '\t'.join(item)

if __name__ == '__main__':
    main()
