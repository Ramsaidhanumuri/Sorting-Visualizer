import random
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get("gen_arr_b"):
            array_len = int(request.POST.get('a_size'))
            gen_arr = generate_array(array_len)
            bc = '#0065d8'
            bi = 'linear-gradient(160deg, #0065d8 0%, #1dcbaf 100%)'
            return render(request, 'index.html', {'gen_arr':gen_arr, 'bc': bc, 'bi':bi})

    if request.POST.get("bubble_sort"):
        if request.POST.get('gen_arr'):
            gen_arr1 = list(map(int, request.POST.get('gen_arr').split(',')))
            b_sort = bubble_sort(gen_arr1)
            tw_case = 'O(N^2)'
            ta_case = 'O(N^2)'
            best_case = 'O(N)'
            avg_space = 'O(1)'
            bc = '#0cb14e'
            bi = 'linear-gradient(160deg, #0cb14e 0%, #f0ec36 100%)'
            return render(
                request, 'index.html', 
                {
                    'gen_arr':b_sort,
                    'tw_case':tw_case,
                    'ta_case':ta_case,
                    'best_case':best_case,
                    'avg_space':avg_space,
                    'bc': bc,
                    'bi':bi
                }
            )
        else:
            messages.error(request, 'Please Generate Array')
            return redirect('index')
    
    elif request.POST.get("selection_sort"):
        if request.POST.get('gen_arr'):
            gen_arr1 = list(map(int, request.POST.get('gen_arr').split(',')))
            b_sort = selection_sort(gen_arr1)
            tw_case = 'O(N^2)'
            ta_case = 'O(N^2)'
            best_case = 'O(N^2)'
            avg_space = 'O(1)'
            bc = '#ff7d0d'
            bi = 'linear-gradient(160deg, #ff7d0d 0%, #ffbc35 100%)'
            return render(
                request, 'index.html', 
                {
                    'gen_arr':b_sort,
                    'tw_case':tw_case,
                    'ta_case':ta_case,
                    'best_case':best_case,
                    'avg_space':avg_space,
                    'bc': bc,
                    'bi':bi
                }
            )
        else:
            messages.error(request, 'Please Generate Array')
            return redirect('index')
    
    elif request.POST.get("merge_sort"):
        if request.POST.get('gen_arr'):
            gen_arr1 = list(map(int, request.POST.get('gen_arr').split(',')))
            call_merge_class = MergeSort()
            b_sort = call_merge_class.mergeSort(gen_arr1)
            tw_case = 'O(N*LogN)'
            ta_case = 'O(N*LogN)'
            best_case = 'O(N*LogN)'
            avg_space = 'O(N)'
            bc = '#08AEEA'
            bi = 'linear-gradient(160deg, #08AEEA 0%, #2AF598 100%)'
            return render(
                request, 'index.html', 
                {
                    'gen_arr':b_sort,
                    'tw_case':tw_case,
                    'ta_case':ta_case,
                    'best_case':best_case,
                    'avg_space':avg_space,
                    'bc': bc,
                    'bi':bi
                }
            )
        else:
            messages.error(request, 'Please Generate Array')
            return redirect('index')

    elif request.POST.get("insertion_sort"):
        if request.POST.get('gen_arr'):
            gen_arr1 = list(map(int, request.POST.get('gen_arr').split(',')))
            b_sort = insertion_sort(gen_arr1)
            tw_case = 'O(N^2)'
            ta_case = 'O(N^2)'
            best_case = 'O(N)'
            avg_space = 'O(1)'
            bc = '#ffce12'
            bi = 'linear-gradient(160deg, #ffce12 0%, #00d4ae 100%)'
            return render(
                request, 'index.html', 
                {
                    'gen_arr':b_sort,
                    'tw_case':tw_case,
                    'ta_case':ta_case,
                    'best_case':best_case,
                    'avg_space':avg_space,
                    'bc': bc,
                    'bi':bi
                }
            )
        else:
            messages.error(request, 'Please Generate Array')
            return redirect('index')
    
    elif request.POST.get("quick_sort"):
        if request.POST.get('gen_arr'):
            gen_arr1 = list(map(int, request.POST.get('gen_arr').split(',')))
            b_sort = QuickSort().quicksorthelper(gen_arr1)
            tw_case = 'O(N^2)'
            ta_case = 'O(N*LogN)'
            best_case = 'O(N*LogN)'
            avg_space = 'O(LogN)'
            bc = '#08AEEA'
            bi = 'linear-gradient(160deg, #08AEEA 0%, #2AF598 100%)'
            return render(
                request, 'index.html', 
                {
                    'gen_arr':b_sort,
                    'tw_case':tw_case,
                    'ta_case':ta_case,
                    'best_case':best_case,
                    'avg_space':avg_space,
                    'bc': bc,
                    'bi':bi
                }
            )
        else:
            messages.error(request, 'Please Generate Array')
            return redirect('index')
    
    elif request.POST.get("heap_sort"):
        if request.POST.get('gen_arr'):
            gen_arr1 = list(map(int, request.POST.get('gen_arr').split(',')))
            b_sort = HeapSort().heapSort(gen_arr1)
            tw_case = 'O(N*LogN)'
            ta_case = 'O(N*LogN)'
            best_case = 'O(N*LogN)'
            avg_space = 'O(1)'
            bc = '#0cb14e'
            bi = 'linear-gradient(160deg, #0cb14e 0%, #f0ec36 100%)'
            return render(
                request, 'index.html', 
                {
                    'gen_arr':b_sort,
                    'tw_case':tw_case,
                    'ta_case':ta_case,
                    'best_case':best_case,
                    'avg_space':avg_space,
                    'bc': bc,
                    'bi':bi
                }
            )
        else:
            messages.error(request, 'Please Generate Array')
            return redirect('index')
        
    return render(request, 'index.html')

def generate_array(array_len):
    arr = []

    for i in range(array_len):
        n = random.randint(20, 150)
        n = (n % 70)+10
        arr.append(n)
    
    return arr

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        mid = i
        for j in range(i+1, n):
            if arr[j]<arr[mid]:
                mid = j
        
        arr[i], arr[mid] = arr[mid], arr[i]
    
    return arr

class MergeSort:
    def mergeSort(self, array):
        if len(array) > 1:
            mid = len(array)//2
            l = array[:mid]
            r = array[mid:]

            self.mergeSort(l)
            self.mergeSort(r)

            i = j = k = 0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    array[k] = l[i]
                    i += 1
                else:
                    array[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                array[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                array[k] = r[j]
                j += 1
                k += 1
                
        return array

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i-1

        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = temp
    return arr

class QuickSort():
    def quicksorthelper(self, arr):
        n = len(arr)
        l = 0
        r = n-1

        return self.helper(arr, l, r)

    def partition(self, arr, l, r):
        i = ( l-1 )
        mid = arr[r]
        for j in range(l , r):
            if arr[j] <= mid:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[r] = arr[r],arr[i+1]

        return ( i+1 )

    def helper(self, arr, l, r):
        if l < r:
            mid = self.partition(arr, l, r)
            self.helper(arr, l, mid-1)
            self.helper(arr, mid+1, r)
        
        return arr

class HeapSort():
    def helper(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.helper(arr, n, largest)

  
    def heapSort(self, arr):
        n = len(arr)

        for i in range(n//2, -1, -1):
            self.helper(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]

            self.helper(arr, i, 0)
        
        return arr