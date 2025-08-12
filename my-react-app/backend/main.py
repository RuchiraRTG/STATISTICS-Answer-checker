from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NumbersInput(BaseModel):
    numbers: List[float]

# ----- Statistics Functions -----
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

def range_calc(A): return max(A) - min(A)
def median(A): 
    n = len(A)
    return (A[n//2 - 1] + A[n//2]) / 2 if n % 2 == 0 else A[n//2]
def Q1(A): return A[len(A)//4 - 1] if len(A) % 2 == 0 else A[len(A)//4]
def Q3(A): return A[3*len(A)//4 - 1] if len(A) % 2 == 0 else A[3*len(A)//4]
def IQR(A): return Q3(A) - Q1(A)
def upper_fence(A): return Q3(A) + 1.5 * IQR(A)
def lower_fence(A): return Q1(A) - 1.5 * IQR(A)
def most_frequent(A): return max(set(A), key=A.count)

@app.post("/calculate")
def calculate(data: NumbersInput):
    A = data.numbers
    sorted_A = insertion_sort(A.copy())
    return {
        "length": len(A),
        "before": A,
        "after": sorted_A,
        "max": max(A),
        "min": min(A),
        "range": range_calc(A),
        "mostFrequent": most_frequent(A),
        "median": median(sorted_A),
        "Q1": Q1(sorted_A),
        "Q3": Q3(sorted_A),
        "IQR": IQR(sorted_A),
        "upperFence": upper_fence(sorted_A),
        "lowerFence": lower_fence(sorted_A)
    }
