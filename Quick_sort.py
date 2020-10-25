import time

def partition(data,head,tail,DrawData,timetick):
    border=head
    pivot=data[tail]                        #head and tail are first and last elements of the array

    DrawData(data,getcolorArray(len(data),head,tail,border,border))        #current index here will be border
    time.sleep(timetick)

    for j in range(head,tail):
        if(data[j]<pivot):
            DrawData(data, getcolorArray(len(data), head, tail, border,j,True))
            time.sleep(timetick)
            data[border],data[j]=data[j],data[border]
            border+=1
        DrawData(data, getcolorArray(len(data), head, tail, border,j))  # current index here will be border
        time.sleep(timetick)

    #swap border element and value
    DrawData(data, getcolorArray(len(data), head, tail, border, tail,True))  # current index here will be border
    time.sleep(timetick)
    data[tail], data[border] = data[border], data[tail]
    return border

def quicksort(data,head,tail,DrawData,timetick):
    if(head<tail):
        q=partition(data,head,tail,DrawData,timetick)

        #left partition
        quicksort(data,head,q-1,DrawData,timetick)


         #right partition
        quicksort(data,q+1,tail,DrawData,timetick)


def getcolorArray(datalen,head,tail,border,currIdx,isSwapping=False):
    colorArray=[]
    for i in range(datalen):
        #base coloring
        if i>=head and i<=tail:
            colorArray.append('grey')
        else:
            colorArray.append('white')

        if i==tail:
            colorArray[i]='blue'
        elif i==border:
            colorArray[i]='red'
        elif i==currIdx:
            colorArray[i]='yellow'

        if isSwapping:
            if i==border or i==currIdx:
                colorArray[i]='green'
    return colorArray