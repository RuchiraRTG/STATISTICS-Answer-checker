# def INSERTION_SORT(A):
 
def INSERTION_SORT(A):
    for j in range(1, len(A)):  
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

def Range(A):
    return max(A) - min(A)

def median(A):
    n = len(A)
    if n % 2 == 0:
        return (A[n//2 - 1] + A[n//2]) / 2
    else:
        return A[n//2]

def Q1(A):
    n = len(A)
    if n % 2 == 0:
        return A[n//4 - 1]   
    else:
        return A[n//4]

def Q3(A):
    n = len(A)
    if n % 2 == 0:
        return A[3 * n // 4 - 1]   
    else:
        return A[3 * n // 4]

def IQR(A):
    return Q3(A) - Q1(A)

def upper_fence(A):
    return Q3(A) + 1.5 * IQR(A)

def lower_fence(A):
    return Q1(A) - 1.5 * IQR(A)

def most_frequent(A):
    return max(set(A), key=A.count)

 
A = []
print("Enter numbers one by one (press Enter on empty line to finish):")
while True:
    value = input("Enter number: ")
    if value == "":  # Stop if blank line
        break
    try:
        A.append(int(value))  # Store as float (or int if needed)
    except ValueError:
        print("Invalid number! Try again.")

 
print("\nlength =", len(A))
print("Before Sorting =", A)
print("After Insertion Sort =", INSERTION_SORT(A.copy()))
print("Maximum Number =", max(A))
print("Minimum Number =", min(A))
print("Range =", Range(A))
print("Most Frequent Number =", most_frequent(A))
print("Median =", median(INSERTION_SORT(A.copy())))
print("First Quartile (Q1) =", Q1(INSERTION_SORT(A.copy())))
print("Third Quartile (Q3) =", Q3(INSERTION_SORT(A.copy())))
print("Interquartile Range (IQR) =", IQR(INSERTION_SORT(A.copy())))
print("Upper Fence =", upper_fence(INSERTION_SORT(A.copy())))
print("Lower Fence =", lower_fence(INSERTION_SORT(A.copy())))

