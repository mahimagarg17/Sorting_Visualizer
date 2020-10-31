from tkinter import *  #importing everyrhing from tkinter
from tkinter import ttk
import random
from bubble_sort import bubblesort
from Quick_sort import quicksort
from merge_sort import mergesort
from Insertion_sort import insertionSort
from Selection_sort import selectionsort
from Heap_Sort import heapSort
root=Tk()
root.title("Sorting algorithm visualizer")
root.maxsize(900,600)
root.config(bg='black')

#variables
selected_alg=StringVar()
data=[]

def DrawData(data,colorArray):
    canvas.delete("all")     #so that if we again call generate previous work or bar graphs will be cleared(screen will be cleared)
    c_height=380
    c_width=600
    x_width=c_width/(len(data)+1) #width of the bar graph
    offset=30
    spacing=10
    normalizedData=[i/max(data) for i in data]
    for i,height in enumerate(normalizedData):
        #topleft corner of rectangle(ith bar)
        x0=i*x_width+ offset+spacing
        y0=c_height-height*340
        #bottom right corner of the ith bar
        x1=(i+1)*x_width +offset
        y1=c_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))    #write the actual number below each bar
    root.update_idletasks()     #Calls all pending idle tasks, without processing any other events   (earlier directly the sorted array was showing but now step by step we'll see each changes)




def Generate():
    global data      #to access the global data array(that we have declared globally)
    minval=int(minEntry.get())
    maxval=int(maxEntry.get())
    size=int(sizeEntry.get())

    data=[]
    for _ in range(size):
        data.append(random.randrange(minval,maxval+1))
    DrawData(data,['red' for x in range(len(data))])      #['red','red','red',...........]

def StartAlgorithm():
    global data

    if not data: return

    if(algmenu.get()=='Quick Sort'):
        quicksort(data,0,len(data)-1,DrawData,speedScale.get())

    elif((algmenu.get()=='Bubble Sort')):
        bubblesort(data,DrawData,speedScale.get())

    elif(algmenu.get()=='Merge Sort'):
        mergesort(data,DrawData,speedScale.get())

    elif(algmenu.get()=='Inertion Sort'):
        insertionSort(data, DrawData,speedScale.get())

    elif (algmenu.get() == 'Selection Sort'):
        selectionsort(data, DrawData, speedScale.get())

    elif (algmenu.get() == 'Heap Sort'):
        heapSort(data, DrawData, speedScale.get())

    DrawData(data, ['green' for x in range(len(data))])

#frame/base layout
#this field is for user interface
s=ttk.Style()
s.configure('TFrame', background='grey')
UI_frame= ttk.Frame(root, style='TFrame',width=600,height=200)
UI_frame.grid(row=0,column=0,padx=10,pady=5)   #The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget.
#padding means the gap between rows and columns


#this is where the visulaization will occur
canvas=Canvas(root,width=600 , height=380,bg='white')
canvas.grid(row=1, column=0,padx=10,pady=5)

#user interface area
#Row[0]
Label(UI_frame, text="Algorithms: ",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)      #
#algmenu represents the drop down list
algmenu=ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort','Quick Sort','Merge Sort','Inertion Sort','Selection Sort','Heap Sort'])  #textvariable parameter : 	A variable linked to the current value of the combobox; when the variable is changed, the current value of the combobox will be updated, while when the user changes the combobox, the variable will be updated.
algmenu.grid(row=0,column=1,padx=5,pady=5)
algmenu.current(0)

#speed scale like a slider to select speed
speedScale=Scale(UI_frame,from_=0.1,to=2.0,length=200,digits=2,resolution=0.2,orient=HORIZONTAL,label="Select Speed[s]")
speedScale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=1,column=4,padx=5, pady=5)

#Row[1]
sizeEntry=Scale(UI_frame,from_=3,to=25,resolution=1,orient=HORIZONTAL,label="Data Size")
sizeEntry.grid(row=1,column=0, padx=5,pady=5)

minEntry=Scale(UI_frame,from_=0,to=10,resolution=1,orient=HORIZONTAL,label="Min Value")
minEntry.grid(row=1,column=1, padx=5,pady=5)

maxEntry=Scale(UI_frame,from_=10,to=100,resolution=1,orient=HORIZONTAL,label="Max Value")
maxEntry.grid(row=1,column=2, padx=5,pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1,column=3,padx=5, pady=5)


root.mainloop()
