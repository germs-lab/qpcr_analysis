#!/usr/bin/python
#this script generage metafile from sample plate
#usage: python meta_sample_to_qpcr_plate.py sample_plate
import sys

def get_num(col):
    num = int(col)
    plate_num = 0
    col_num = [0,0,0]
    if num == 1:
        plate_num = 1
        col_num = [4,5,6]
    elif num == 2:
        plate_num = 1
        col_num = [7,8,9]
    elif num == 3:
        plate_num = 1
        col_num= [10,11,12]
    elif num == 4:
        plate_num = 2
        col_num= [4,5,6]
    elif num == 5:
        plate_num = 2
        col_num= [7,8,9]
    elif num == 6:
        plate_num = 2
        col_num= [10,11,12]
    elif num == 7:
        plate_num = 3
        col_num= [4,5,6]
    elif num == 8:
        plate_num = 3
        col_num= [7,8,9]
    elif num == 9:
        plate_num = 3
        col_num= [10,11,12]
    elif num == 10:
        plate_num = 4
        col_num= [4,5,6]
    elif num == 11:
        plate_num = 4
        col_num= [7,8,9]
    elif num == 12:
        plate_num = 4
        col_num= [10,11,12]
    else:
        print "unknown number"

    return plate_num, col_num

def read_meta(file):
    d = {}
    for n,line in enumerate(open(file,'r')):
        if n == 0:
            continue
        spl = line.strip().split(',')
        if int(spl[2]) < 10:
            ids = spl[1]+"0"+spl[2]
        else:
            ids = spl[1]+spl[2]
        d[ids] = spl
    return d
    
def main():
    d = read_meta(sys.argv[1])
    for ids, item in d.items():
        #print ids, item
        plate_num, colnum = get_num(item[2])
        for x in colnum:
            co = ""
            if x < 10:
                co = item[1] + "0" + str(x)
            else:
                co = item[1] + str(x)
            result = ["plate_"+str(plate_num),co, '\t'.join(item)]
            print '\t'.join(result)

if __name__ == '__main__':
    main()
