# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import itertools as it


def iterateCase(s):
    lu_sequence = ((c.lower(), c.upper()) for c in s)
    return [''.join(x) for x in it.product(*lu_sequence)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bigList=[]
    bigList.extend(iterateCase('LBEList'))
    bigList.extend(iterateCase('MDvotes22'))
    bigList.extend(iterateCase('StatusSearch'))
    bigList.extend(iterateCase('NeedBallot'))
    bigList.extend(iterateCase('LBElist'))
    bigList.extend(iterateCase('MDagent'))

    for b, base in enumerate(bigList):
        bigList[b]="http://bit.ly/"+base

    textfile = open(r"F:\Projects\Python\apivoid\Python3\example16\urls.txt", "w")
    for element in bigList:
        textfile.write(element + "\n")
    textfile.close()

    #print(len(bigList))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
