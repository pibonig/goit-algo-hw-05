from typing import List, Tuple


def binary_search(arr: List[float], target: float) -> Tuple[int, float]:
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = float('inf')

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = min(upper_bound, arr[mid])
            right = mid - 1

    return iterations, upper_bound


if __name__ == "__main__":
    arr = [0.1, 0.5, 1.2, 2.3, 3.4, 4.8, 5.9]
    target = 2.5
    result = binary_search(arr, target)

    print(f"Number of iterations: {result[0]}, Upper bound: {result[1]}")
