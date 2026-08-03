import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    STEPS = [5, 3, 1]
    TARGET = 17
    return STEPS, TARGET


@app.function
def step_combinations(
    remaining: int,
    steps: list[int],
    chosen: tuple[int, ...] = (),
):
    step = steps[0]

    if len(steps) == 1:
        if remaining % step == 0:
            yield chosen + (remaining // step,)
        return

    for amount in range(remaining // step + 1):
        new_remaining = remaining - amount*step
        yield from step_combinations(
            new_remaining,
            steps[1:],
            chosen + (amount,)
        )


@app.cell
def _(STEPS, TARGET):
    from pprint import pprint

    pprint([_ for _ in step_combinations(TARGET, STEPS)])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
