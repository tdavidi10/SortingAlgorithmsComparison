






from tkinter import *
from tkinter import ttk
from SortingAlgorithms import *
import random
import timeit
import multiprocessing




root  = Tk()
root.title("Sorting Algorithms Comparison") # title
root.iconbitmap('C:/Users/Tamir/Sorting/sort_icon.ico') #icon
screen_width = root.winfo_screenwidth() ### centering the window
screen_height = root.winfo_screenheight()

window_width = 1024
window_height = 768

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2) - 50

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') ### centering the window

# head label
head_label = Label(root, text= "Sorting Competition", font=("Tahoma", 18))
head_label.pack(pady=20)

# choose array size label
array_size_label = Label(root, text= "type the size of the array you would like to sort (size:0-1000)", font=("Tahoma", 14))
array_size_label.pack(pady=20)

# array size textbox
size_text_box = Text(root, width=5, height=1, font=("Tahoma", 12))
size_text_box.pack(pady=20)
    
tv = ttk.Treeview(root)
num_of_clicks = 0
# clicking start: making table and sorting
def start_button_click():
    global tv
    tv.delete(*tv.get_children())
    global num_of_clicks
    num_of_clicks = num_of_clicks + 1
    # "winner is..." label
    if num_of_clicks == 1: # in the first click
        sort_label = Label(root, text= "And The Winner Is...", font=("Tahoma", 14))
        sort_label.pack(pady=20)        

    # generate "size" long random list which we will sort in differenr way
    size = int(size_text_box.get(1.0, END))
    lst = []
    for i in range(size): # adds "size" random numbers between 0 - 1000000
        lst.append(random.randint(0,100))

    # actuall sorting:
    results = {} # results dict: key - name of alg, val - runtime
    algorithms = [quickSort, mergeSort, heapSort, bubbleSort, insertionSort, selectionSort, TimSort]
    for alg in algorithms:
        lst_to_sort = lst.copy()
        if alg in {quickSort, heapSort}: # in-place sorting algorithms add here
            start = timeit.default_timer() # start timer
            alg(lst_to_sort) # execute sort - notice it's in place
            stop = timeit.default_timer() # stop timer
        else: # not int-place sorting algorithms
            start = timeit.default_timer() # start timer
            lst_to_sort = alg(lst_to_sort) # execute sort - notice it's not in-place
            stop = timeit.default_timer() # stop timer
        
        results[alg.__name__] = stop - start # insert alg runtime to dict

    # sort the algorithms by their runtime and moving it to sordet data structure-list
    result_sorted_lst = sorted(results.items(), key=lambda item: item[1])

    # creating table
    # setting columns
    tv['columns']=('Name', 'Runtime', 'Complexity')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=CENTER, width=200)
    tv.column('Runtime', anchor=CENTER, width=200)
    tv.column('Complexity', anchor=CENTER, width=200)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Runtime', text='Runtime', anchor=CENTER)
    tv.heading('Complexity', text='Complexity', anchor=CENTER)

    # setting values in the table
    i = 0
    for pair in result_sorted_lst: # for every pair-algname, runtime       
        # O(nlogn)
        if pair[0] in {mergeSort.__name__, heapSort.__name__, TimSort.__name__}: 
            tv.insert(parent='', index=i, iid=i, text='', values=(pair[0], str(pair[1]),'O(nlogn)'))
        # O(nlogn) on average
        elif pair[0] in {quickSort.__name__}: 
            tv.insert(parent='', index=i, iid=i, text='', values=(pair[0], str(pair[1]),'O(nlogn) on average'))
        else: # O(n^2)
            tv.insert(parent='', index=i, iid=i, text='', values=(pair[0], str(pair[1]),'O(n^2)'))

        i = i + 1  
    
    tv.pack()




# start button init
start_button = Button(root, text= "Start Sorting!", padx= 20, pady= 10, command=start_button_click)
start_button.pack(pady=10) 

root.mainloop()


