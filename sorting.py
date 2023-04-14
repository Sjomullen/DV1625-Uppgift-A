def quicksort(lst: list) -> None:
    def Quick(p, r):
        if p < r:
            x = lst[r]
            i = p -1 

            for j in range(p, r):
                if lst[j] <= x:
                    i = i + 1
                    lst[i], lst[j] = lst[j], lst[i]
            lst[i + 1], lst[r] = lst[r], lst[i + 1]

            
            q = i + 1   
            Quick(p, q - 1)
            Quick(q + 1, r)
    Quick(0, len(lst) - 1)
        
      

                

def insertionsort(lst: list) -> None:
   
   for i in range(1, len(lst)):
       key = lst[i]
       j = i -1
       
       while j >= 0 and lst[j] > key:
           lst[j + 1] = lst[j]
           j = j -1
       lst[j + 1] = key 
       
def mergesort(lst: list) -> None:
    def MergeSort(p, r):
        if p < r:
            q = (p + r) // 2
            MergeSort(p, q)
            MergeSort(q + 1, r)
            Merge(p, q, r)

    def Merge(p, q, r):
        n1 = q - p + 1
        n2 = r - q

        L = [None] * (n1 + 2)
        R = [None] * (n2 + 2)

        for i in range(n1):
            lst[i] = lst[p + i - 1]
        
        for j in range(n2):
            lst[j] = lst[q + j]

        L[n1 + 1] = None
        R[n2 + 1] = None

        i = 1
        j = 1

        for k in range(p, r + 1):
            if L[i] < R[j]:
                lst[k] = L[i]
                i = i + 1
            else:
                lst[k] = R[j]
                j = j + 1
    MergeSort(0, len(lst) - 1)


def mergesort_hybrid(lst: list) -> None:
    pass

def quicksort_hybrid(lst: list) -> None:
    pass
