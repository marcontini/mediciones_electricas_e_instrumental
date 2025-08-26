import numpy as np


def u_i(arr: list, ddof: int = 1) -> float:
    return np.array(arr).std(ddof=ddof) / np.sqrt(len(arr))


def mean(arr: list) -> float:
    return np.array(arr).mean()


def std(arr: list, ddof: int = 1) -> float:
    return np.array(arr).std(ddof=ddof)


def fprint(title: str, value, unit: str, decimals: int = 4) -> None:
    print(f"{title:<10}{round(value, decimals):>10} {unit}")


def semrng(arr: list, err_inst: float = 0.0) -> list:
    arr_med = mean(arr)
    sem = arr_med * err_inst
    return (sem, arr_med - sem, arr_med + sem)


def u_j(arr: list, sem=0.0, k=1) -> float:
    return sem / np.sqrt(k)
