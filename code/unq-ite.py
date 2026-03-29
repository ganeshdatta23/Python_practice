import logging
import time


def measure(label, fn):
    start = time.perf_counter()
    result = fn()
    duration = time.perf_counter() - start
    logging.info("%s took %.6fs -> %s", label, duration, result)
    return result


def unique_manual(seq):
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def unique_dict(seq):
    return list(dict.fromkeys(seq))


def unique_set(seq):
    return list(set(seq))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    itr = [i for i in range(1000) for _ in range(10)]

    measure("manual (preserve order)", lambda: unique_manual(itr))
    measure("dict.fromkeys (preserve order)", lambda: unique_dict(itr))
    measure("set (unordered)", lambda: unique_set(itr))
