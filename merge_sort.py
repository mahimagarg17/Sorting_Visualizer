import time

def mergesort(data,DrawData,timetick):

    mergeSort_alg(data,0,len(data)-1,DrawData,timetick)

def merge(data, l, m, r,DrawData,timetick):
    DrawData(data,getColorArray(len(data),l,m,r))
    time.sleep(timetick)

    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = data[l + i]

    for j in range(0, n2):
        R[j] = data[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1

    DrawData(data, ["green" if x>=l and x<=r else "white" for x in range(len(data))])
    time.sleep(timetick)


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort_alg(data, l, r,DrawData,timetick):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort_alg(data, l, m,DrawData,timetick)
        mergeSort_alg(data, m + 1, r,DrawData,timetick)
        merge(data, l, m, r,DrawData,timetick)

def getColorArray(length,left,middle,right):
    colorarray=[]

    for i in range(length):
        if i>=left and i<=right:
            if(i>=left and i<=middle):
                colorarray.append("yellow")              #left part of the array would be yellow
            else:
                colorarray.append("pink")                #right part of the array would be pink
        else:
            colorarray.append("white")                   #the array that you are not working with would be white

    return colorarray