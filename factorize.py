import time
import multiprocessing

def factorize(*numbers):
    results = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        results.append(factors)
    return results

def sync_factorize(numbers):
    results = []
    for number in numbers:
        results.append(factorize(number))
    return results

# Паралельна версія факторизації
def parallel_factorize(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results


def test_factorize():
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


result = factorize(128, 255, 99999, 10651060)


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    # Виміряйте час виконання для синхронної версії
    start_time = time.time()
    sync_results = sync_factorize(numbers)
    end_time = time.time()
    print(f"Sync Execution Time: {end_time - start_time} seconds")

    # Виміряйте час виконання для паралельної версії
    start_time = time.time()
    parallel_results = parallel_factorize(numbers)
    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time} seconds")

    # Перевірка результатів
    for i in range(len(numbers)):
        assert sync_results[i] == parallel_results[i]