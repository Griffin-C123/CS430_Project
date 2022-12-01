import os


def parseFile(name):
    # Creates the sets based off the instance file given
    file = open(name, "r")
    line = file.readline()
    m, n, k, p = line.split()
    collection = {}
    # loops through each line of the file to parse information
    for i in range(int(p)):
        line = file.readline()
        i, j = line.split()
        i, j = int(i), int(j)
        if i in collection.keys():
            collection[i].add(j)
        else:
            collection[i] = set()
            collection[i].add(j)
    file.close()
    # creates all subsets of a universe of n elements
    collection["U"] = set([x for x in range(1, int(n) + 1)])
    return int(m), int(k), collection


def maximumCoverage(collection, k, m):
    # algorithm - currently just takes the smallest number from each set and puts them in a new set for testing purposes
    ret = set()
    for i in range(1, m + 1):
        ret.add(min(collection[i]))
    return f"min({k}, {m}): {ret}"


def writeFile(name, content):
    # writes to the file
    file = open(name, "w")
    file.write(content)
    file.close()


path = input("Enter the path to instance.txt files (more info in README)\n")

try: os.mkdir("solutions")
except: pass

iteration = 1

while os.path.exists(path + f"instance{str(iteration).zfill(2)}.txt"):
    # m is the number of sets in the file, number k for the algorithm
    m, k, collection = parseFile(path + f"instance{str(iteration).zfill(2)}.txt")
    writeFile("solutions/" + f"solution{str(iteration).zfill(2)}.txt", maximumCoverage(collection, k, m))
    print(collection)
    iteration += 1
