import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    def next_collatz(n: int) -> int:
        if n % 2 == 0:
            return n // 2
        return 3*n + 1

    def collatz_sequence_starting(n: int) -> list[int]:
        res = [n]
        while n != 1:
            n = next_collatz(n)
            res.append(n)
        return res

    return (collatz_sequence_starting,)


@app.cell
def _(collatz_sequence_starting):
    max_length = 0
    n_max = 1
    for n in range(2, 10**6):
        seq = collatz_sequence_starting(n)
        l_seq = len(seq)
        if l_seq > max_length:
            max_length = l_seq
            n_max = n
    return (n_max,)


@app.cell
def _(n_max):
    n_max
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
