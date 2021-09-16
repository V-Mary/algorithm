import time

start_time = time.time()

comparison = 0


def merge_sort(arr, type_merge):

    global comparison

    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, type_merge)
        merge_sort(R, type_merge)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if type_merge == "asc":
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                    comparison += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    comparison += 1
                k += 1

            elif type_merge == "desc":
                if L[i] > R[j]:
                    arr[k] = L[i]
                    i += 1
                    comparison += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    comparison += 1
                k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def main():
    print("MergeSort:")

    type_merge = input("Sort array in asc or desc?:")

    print("Please, enter an array:")
    arr = input().split(",")

    merge_sort(arr, type_merge)
    print(f"Sorted array is:", arr)

    print("execution time:", time.time() - start_time)

    print("Comparisons:", comparison)


if __name__ == "__main__":
    main()