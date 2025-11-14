# plot_results.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

for kind in df['kind'].unique():
    sub = df[df['kind'] == kind]
    plt.figure()
    for alg in ['deterministic','randomized']:
        x = sub[sub['algorithm'] == alg]['n']
        y = sub[sub['algorithm'] == alg]['avg_time']
        plt.plot(x, y, marker='o', label=alg)
    plt.xlabel('n')
    plt.ylabel('avg time (s)')
    plt.title(f'Quicksort running time — {kind}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'plot_{kind}.png')
