import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import sympy

    return (sympy,)


@app.cell
def _(sympy):
    def divisor_sum(n: int) -> int:
        dn = sympy.divisors(n)[:-1]
        return sum(dn)

    divsum_dict = {k: divisor_sum(k) for k in range(1, 10001)}
    amicable_numbers = set()

    for a, b in divsum_dict.items():
        if divsum_dict.get(b) == a and a != b:
            amicable_numbers = amicable_numbers | {a, b}

    print(sum(amicable_numbers))
    return


if __name__ == "__main__":
    app.run()
