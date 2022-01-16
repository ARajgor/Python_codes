capacity = 4
processList = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

s = []

pageFaults = 0
pointer = 0
hit = 0

for i in processList:

    if i not in s:

        if len(s) == capacity:
            f = processList[pointer-1]  # find_mru
            find = s.index(f)   # find_mru_in_s
            s.remove(f)
            s.insert(find, i)   # Remove_and_add

        else:
            s.append(i)

        pageFaults += 1

    else:
        hit = hit + 1

    pointer = pointer + 1

print("PageFaults: ", pageFaults)
print("Hit: ", hit)
