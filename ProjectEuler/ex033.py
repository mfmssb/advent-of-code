import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy import fraction, Rational
    from functools import reduce
    from pprint import pprint

    return Rational, fraction, pprint, reduce


@app.cell
def _(Rational, fraction, pprint, reduce):
    def freshman_simplification(num: int, den: int) -> tuple[int, int]:
        numstr = str(num)
        denstr = str(den)

        common_digits = [d for d in numstr if d in denstr]
    
        if not len(common_digits) == 1:
            return (num, den)
    
        common_digit = common_digits[0]
        if common_digit == "0":
            return (num, den)

        n_i = numstr.find(common_digit)
        d_i = denstr.find(common_digit)
        new_num = numstr[:n_i] + numstr[n_i+1:]
        new_den = denstr[:d_i] + denstr[d_i+1:]
    
        return (int(new_num), int(new_den))

    freshmans = set()
    for a in range(10, 99):
        for b in range(a+1, 100):
            c, d = fraction(Rational(a, b))
            e, f = freshman_simplification(a, b)
            num, den = fraction(Rational(e, f))

            if (num, den) == (c, d) and (a, b) != (e, f):
                pprint(f"{a}/{b} = {c}/{d} ?= {e}/{f} = {num}/{den}")
                freshmans.add((a, b))
    f_list = list(freshmans)

    f_list = [Rational(a, b) for a, b in f_list]
    print(reduce(lambda x, y: x*y, f_list).denominator)
    return


if __name__ == "__main__":
    app.run()
