import time

def selectionsort(data,DrawData,timetick):
    for i in range(len(data)):
        time.sleep(timetick)
    # Find the minimum element in remaining
    # unsorted array
        min_idx = i
        for j in range(i + 1, len(data)):

            if data[min_idx] > data[j]:
                min_idx = j
                DrawData(data,["blue" if x==min_idx else "white" for x in range(len(data))])
                time.sleep(timetick)

            # Swap the found minimum element with
    # the first element
        data[i], data[min_idx] = data[min_idx], data[i]
        DrawData(data, ["green" if x == i else "yellow" if x==min_idx else "white" for x in range(len(data))])
        time.sleep(timetick)

