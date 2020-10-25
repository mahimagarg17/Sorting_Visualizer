import time

#this function builts the max heap
def heapify(arr, n, i,DrawData,timetick):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        DrawData(arr,["blue" if x==i or x==largest else "red" for x in range(len(arr))])
        time.sleep(timetick)

        # Heapify the root.
        heapify(arr, n, largest,DrawData,timetick)

    # The main function to sort an array of given size


def heapSort(arr,DrawData,timetick):
    n = len(arr)

    # Build a maxheap.(in a maxheap node is always greater than the child nodes)
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i,DrawData,timetick)
    DrawData(arr, ["blue" for x in range(len(arr))])
    time.sleep(timetick)
        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        DrawData(arr, ["green" if x==i or x==0 else "red" for x in range(len(arr))])
        time.sleep(timetick)

        heapify(arr, i, 0,DrawData,timetick)

    # Driver code to test above
