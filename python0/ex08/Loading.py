import os

class Ft_tqdm:
    def __init__(self, r: range):
        self.n = 0
        self.r = r
    def __iter__(self):

    def __next__(self):
        percent = (self.n / self.r[-1]) * 100
        print(f"\r" + percent + "%| [", end="")
    n: int
    r: range
def ft_tqdm(lst: range) -> None:
    c = Ft_tqdm(lst)
    return(c)
