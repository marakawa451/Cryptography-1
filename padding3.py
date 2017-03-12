#!/usr/bin/python3

import requests
import string

allhex = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "1A", "1B", "1C", "1D", "1E", "1F", 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, "2A", "2B", "2C", "2D", "2E", "2F", 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, "3A", "3B", "3C", "3D", "3E", "3F", 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, "4A", "4B", "4C", "4D", "4E", "4F", 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, "5A", "5B", "5C", "5D", "5E", "5F", 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, "6A", "6B", "6C", "6D", "6E", "6F", 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, "7A", "7B", "7C", "7D", "7E", "7F", 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, "8A", "8B", "8C", "8D", "8E", "8F", 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, "9A", "9B", "9C", "9D", "9E", "9F", 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF','E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'EA', 'EB', 'EC', 'ED', 'EE', 'EF','F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF']
allhex = list(map(str, allhex))

#fullstring = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
qstring = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd'


def splice_ct():
    return qstring[-2:]

def new_qstring():
    return qstring[:-2]

def xorb(a,b):
        return bytes(x^y for x,y in zip(a,b))

def triple(ct, pt, pad):
        xora = xorb(bytes.fromhex(ct),bytes.fromhex(pt))
        xorc = xorb(xora,bytes.fromhex(pad))
#       print(str(xora.hex()))
        return (str(xorc.hex()))

pad_range = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]

#def compute_pad(ct, pt, pad):
#         (triple(ct, pt, pad))
#        print(endstring)

#compute_pad("10")

def search(ct, pad, rquery, ender):
  for i in allhex:
        xori = xorb(bytes.fromhex(i),bytes.fromhex(ct))
        xori2 = xorb(xori, bytes.fromhex(pad))
        strxori = str(xori2.hex())
        r = requests.get('http://crypto-class.appspot.com/po?er=' + rquery + strxori + ender)
        if r.status_code == 404:
                return(i)
#                print(xori)
#                print(xori2)
               # print(strxori)
#                print(r.status_code)
                break

def new_endstring(new_pad):
    return str(new_pad) + endstring

def create_pad(nums):
    if (nums + 1) <= 9:
        return( "0" + str(nums + 1))
    else:
        return(str(nums + 1))

ct_list = []
pt_list = []

for i in range():
    endstring = '4a61044426fb515dad3f21f18aa577c0'
    ct_list.append(qstring[-2:])
    qstring = qstring[:-2]
    print(endstring)
    cpad = create_pad(i)
    for x,y in zip(ct_list, pt_list):
       endstring = str(triple(x, y, (cpad + endstring))
    pt_list.append(search(ct_list[i], cpad , qstring, endstring))
    print(pt_list[i], ct_list[i], i)
    print(qstring)
    print(endstring)

print(pt_list)
print(ct_list)
#auto()
#if __name__ == "__main__":
 #   main()
