import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy import sieve

    return (sieve,)


@app.cell
def _(sieve):
    primes = set([i for i in sieve.primerange(10**6)])
    return (primes,)


@app.function
def quad_formula(n: int, a: int, b: int) -> int:
    return n**2 + a*n + b


@app.cell
def _(primes):
    max_score = []
    num_primes_max = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            current_primes = []
            while True:
                f_of_n = quad_formula(n, a, b)
                if f_of_n in primes:
                    current_primes.append(f_of_n)
                    n += 1
                    if n >= 10**4:
                        print("n too large", a, b)
                        break
                else:
                    current_num_primes = len(current_primes)
                    if current_num_primes > num_primes_max:
                        num_primes_max = current_num_primes
                        max_score.append((a, b, current_num_primes, current_primes))
                    break
    return (max_score,)


@app.cell
def _(max_score):
    final_a = max_score[-1][0]
    final_b = max_score[-1][1]
    ans = final_a * final_b
    print(ans)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
