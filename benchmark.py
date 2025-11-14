# benchmark.py
import random
import time
import statistics
import tracemalloc
import csv
from quicksort import deterministic_quicksort, randomized_quicksort

def generate_array(n, kind='random'):
    if kind == 'random':
        return [random.randint(0, n*10) for _ in range(n)]
    elif kind == 'sorted':
        return list(range(n))
    elif kind == 'reversed':
        return list(range(n, 0, -1))
    elif kind == 'repeated':
        return [random.randint(0, 10) for _ in range(n)]
    else:
        raise ValueError('Unknown kind')

def time_sort(func, arr):
    a = arr.copy()
    tracemalloc.start()
    t0 = time.perf_counter()
    func(a)
    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return t1 - t0, peak

def run_benchmarks(sizes, kinds, repeats=5, random_repeats=10):
    rows = []
    for n in sizes:
        for kind in kinds:
            for alg_name, func, reps in [
                    ('deterministic', deterministic_quicksort, repeats),
                    ('randomized', randomized_quicksort, random_repeats if alg_name=='randomized' else repeats)
                ]:
                times = []
                mems = []
                for r in range(reps):
                    arr = generate_array(n, kind)
                    t, peak = time_sort(func, arr)
                    times.append(t)
                    mems.append(peak)
                rows.append({
                    'n': n,
                    'kind': kind,
                    'algorithm': alg_name,
                    'avg_time': statistics.mean(times),
                    'stdev_time': statistics.stdev(times) if len(times)>1 else 0.0,
                    'avg_mem': statistics.mean(mems)
                })
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['n','kind','algorithm','avg_time','stdev_time','avg_mem']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return rows

if __name__ == '__main__':
    sizes = [1000, 5000, 10000, 50000]   # adjust as needed
    kinds = ['random', 'sorted', 'reversed', 'repeated']
    run_benchmarks(sizes, kinds)
