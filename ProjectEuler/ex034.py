import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    def factorial(n: int) -> int:
        if n == 1 or n == 0:
            return 1
        return n*factorial(n-1)

    def fact_digits(n: int) -> int:
        nstr = str(n)
        return sum([f_dict[int(d)] for d in nstr])

    f_dict = {k: factorial(k) for k in range(0, 10)}
    return f_dict, fact_digits


@app.cell
def _(f_dict, fact_digits):
    sum_ = 0
    UPPERBOUND = len(str(f_dict[9]*len(str(f_dict[9]))))
    for n in range(10**UPPERBOUND):
        if n == fact_digits(n) and n not in [1, 2]:
            print(n)
            sum_ += n
    return


if __name__ == "__main__":
    app.run()
