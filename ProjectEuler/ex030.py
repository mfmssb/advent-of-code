import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    def digit_sum_of_powers(n: int, p: int) -> bool:
        digits = [int(d) for d in str(n)]
        digits_of_power_p = [d**p for d in digits]

        return n == sum(digits_of_power_p)

    assert digit_sum_of_powers(1634, 4)
    assert digit_sum_of_powers(8208, 4)
    assert digit_sum_of_powers(9474, 4)
    return (digit_sum_of_powers,)


@app.cell
def _():
    p = 5
    return (p,)


@app.cell
def _(p):
    upper_bound = 1
    while True:
        n = int("9"*upper_bound)
        sum_powers = sum([9**p for _ in range(upper_bound)])

        if sum_powers < n:
            break
        upper_bound += 1
        if upper_bound > 20:
            break
    return (upper_bound,)


@app.cell
def _(digit_sum_of_powers, p, upper_bound):
    sum_ = 0
    for i in range(2, 10**upper_bound):
        if digit_sum_of_powers(i, p):
            print(i)
            sum_ += i
    print(sum_)
    return


if __name__ == "__main__":
    app.run()
