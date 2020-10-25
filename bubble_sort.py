import time


def bubblesort(data,DrawData,timeTick):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]     #swap them
                DrawData(data,['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)

    DrawData(data,['green' for x in range(len(data))])          #when whole array sorted all bars will be green