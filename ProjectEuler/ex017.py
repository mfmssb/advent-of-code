import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    num_lang = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
    }
    return (num_lang,)


@app.cell
def _(num_lang):
    def read_number(n: int) -> str:
        """
        From 1 to 1000
        """

        nstr = str(n)
        current_nstr = nstr
        res = ""

        while (len(current_nstr) > 0):
            current_num_digits = len(current_nstr)
            current_key = int(current_nstr)
            current_digit = int(current_nstr[0])
            i = 0
            while True:
                i += 1
                if current_key <= 20:
                    current_nstr = ""
                    break
        
                if len(str(current_key)) > 1:
                    current_key = round(current_key // 10**i) * 10**i

                if num_lang.get(current_key):
                    break

                current_test_key = int("1" + str(current_key)[1:])
        
                if num_lang.get(current_test_key):
                    current_key = current_test_key
                    break
        
                if i > 3:
                    break

            if current_key == 0:
                break
            # print(n, res)
            if len(current_nstr) > 2:
                res += num_lang[current_digit] + " "
            # print(res)
            if current_num_digits == 2 and len(nstr) >= 3:
                res += "and "
            # print(res)
            res += num_lang[current_key] + " "
            # print(res)
            current_nstr = current_nstr[1:]
        return res.strip()

    return (read_number,)


@app.cell
def _(read_number):
    test_numbers = [4, 13, 99, 105, 184, 321, 444, 999, 1000]
    for n in test_numbers:
        print(f"{n:5}: {read_number(n)}")
    return


@app.cell
def _():
    # for num in range(1, 1001):
    #     print(f"{num:5}: {read_number(num)}")
    return


@app.cell
def _(read_number):
    num_lang_list = [read_number(num).replace(" ", "") for num in range(1, 1001)]  # remove spaces
    num_lang_list_lengths = [len(x) for x in num_lang_list]
    return (num_lang_list_lengths,)


@app.cell
def _(num_lang_list_lengths):
    print(sum(num_lang_list_lengths))
    return


if __name__ == "__main__":
    app.run()
