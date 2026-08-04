import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import itertools
    from pprint import pprint

    return


@app.function
def combine_digits(l: list):
    return int(("").join([str(d) for d in l]))


@app.cell
def _():
    # digits = [i for i in range(1, 10)]
    # pandigitals = set()

    # split_points = [
    #     (1, 5),  # 1 siffer × 4 sifre = 4 sifre
    #     (2, 5),  # 2 sifre × 3 sifre = 4 sifre
    # ]

    # for comb in itertools.permutations(digits):
    #     for i, j in split_points:
    #         a = comb[:i]
    #         b = comb[i:j]
    #         c = comb[j:]
    #         ad = combine_digits(a)
    #         bd = combine_digits(b)
    #         cd = combine_digits(c)
    #         sorted_triple = sorted([ad, bd, cd])
    #         if ad * bd == cd:
    #             pandigitals.add(cd)

    # sum(pandigitals)
    return


@app.function
def digits_to_int(digits):
    return int("".join(map(str, digits)))


@app.cell
def _():
    # recursive try
    def pandigital_products(
        remaining: tuple[int, ...],
        lengths: tuple[int, int],
        chosen: tuple[int, ...] = (),
    ):
        a_length, b_length = lengths
        required_length = a_length + b_length

        if len(chosen) == required_length:
            a = digits_to_int(chosen[:a_length])
            b = digits_to_int(chosen[a_length:])

            product = a * b
            product_digits = tuple(map(int, str(product)))

            if (
                len(product_digits) == 4
                and sorted(product_digits) == sorted(remaining)
            ):
                yield a, b, product

            return

        for digit in remaining:
            new_remaining = tuple(
                value for value in remaining
                if value != digit
            )

            yield from pandigital_products(
                new_remaining,
                lengths,
                chosen + (digit,),
            )
    digits = tuple(range(1, 10))
    products = set()

    for lengths in [(1, 4), (2, 3)]:
        for a, b, product in pandigital_products(
            digits,
            lengths,
        ):
            products.add(product)
    return (products,)


@app.cell
def _(products):
    products
    return


if __name__ == "__main__":
    app.run()
