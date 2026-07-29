import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.function
def reduce_once(l: list, prime: int) -> list:
    return [prime] + [i for i in l if i % prime != 0]


@app.function
def get_list_of_primes_below(n: int) -> list[int]:
    num_list = list(range(2, n + 1))
    i = 0
    
    while i < len(num_list) - 1:
        prime = num_list[i]
        num_list = sorted(reduce_once(num_list, prime))
        i += 1
    return num_list


@app.cell
def _():
    primes = get_list_of_primes_below(200000)
    return (primes,)


@app.cell
def _(primes):
    prime_number = 10001
    prime_index = prime_number - 1
    primes[prime_index]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
