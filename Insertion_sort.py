import time
def insertionSort(data,DrawData,timetick):
    # Traverse through 1 to len(arr)
    for i in range(1, len(data)):

        key = data[i]
        DrawData(data, ['pink' if x == i else 'white' for x in range(len(data))])
        time.sleep(timetick)

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            DrawData(data, ['yellow' if x == j else 'white' for x in range(len(data))])
            time.sleep(timetick)
            j -= 1

        data[j + 1] = key
