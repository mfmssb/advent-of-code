import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy import divisors, divisor_count

    return (divisor_count,)


@app.function
def triangle_number(n: int) -> int:
    return n*(n+1) // 2


@app.cell
def _(divisor_count):
    max_num_div = 0
    for n in range(10**9):
        t = triangle_number(n)
        num_div = divisor_count(t)
        if num_div > max_num_div:
            print(n, t, num_div)
            max_num_div = num_div
        if max_num_div > 500:
            print("DONE", n, t ,max_num_div)
            break
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
