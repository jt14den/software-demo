import numpy as np

def analyze_data():
    data = np.random.normal(0, 1, 1000)
    print(f'Mean: {np.mean(data)}')
    print(f'Std: {np.std(data)}')

if __name__ == '__main__':
    analyze_data()

