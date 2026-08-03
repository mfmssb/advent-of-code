import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    COINS = [200, 100, 50, 20, 10, 5, 2, 1]
    TARGET = 200


    def coin_combinations(
        remaining: int,
        coins: list[int],
        chosen: tuple[int, ...] = (),
    ):
        coin = coins[0]

        if len(coins) == 1:
            if remaining % coin == 0:
                yield chosen + (remaining // coin,)
            return

        for amount in range(remaining // coin + 1):
            new_remaining = remaining - amount * coin

            yield from coin_combinations(
                new_remaining,
                coins[1:],
                chosen + (amount,),
            )

    return COINS, TARGET, coin_combinations


@app.cell
def _(COINS, TARGET, coin_combinations):
    total = sum(1 for _ in coin_combinations(TARGET, COINS))
    print(total)
    return


if __name__ == "__main__":
    app.run()
