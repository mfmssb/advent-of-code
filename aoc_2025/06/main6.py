# %%
import pandas as pd
from pathlib import Path

# %%
def parse_data_p1(data_path: str) -> list[list[str]]:    
    data: list[str] = Path(data_path).read_text().split("\n")
    data2 = [line.split(" ") for line in data]
    data3 = [[x for x in line if x != ""] for line in data2]
    
    # Make sure that the each line in input data is equally long
    assert [len(line) == len(line[0]) for line in data3]  
    return data3

def convert_data_to_dataframe_p1(data) -> pd.DataFrame:
    df = (
        pd.DataFrame(data)
        .sort_index(ascending=False)
        .reset_index(drop=True)
        .transpose()
        .rename(columns={0: "op"})
    )
    val_cols = [col for col in df.columns if col != "op"]
    df[val_cols] = df[val_cols].apply(pd.to_numeric, errors="coerce")

    df["result_mult"] = df.loc[df["op"] == "*"][val_cols].prod(axis=1)
    df["result_sum"] = df.loc[df["op"] == "+"][val_cols].sum(axis=1)
    df["result"] = df["result_sum"].fillna(df["result_mult"])

    return df

def p1(data) -> int:
    df = convert_data_to_dataframe_p1(data)
    return int(df["result"].sum())
# %%
def parse_data_p2(data_path: str) -> list[list[str]]:    
    data: list[str] = Path(data_path).read_text().split("\n")
    operations = data[-1].split()
    data.pop()
    return data, operations

def p2(data_path):
    """
    Parse data by separating the values and the operations.
    Use Pandas to construct the vertical numbers from input data.
    Use cumulative sum of empty rows to group numbers for each operation (+, *).
    Filter dataset by operation column "op" and calculate the result depending
    on the operation.
    """
    
    values, operations = parse_data_p2(data_path)

    df = (
        pd.DataFrame([list(string) for string in values])
        .transpose()
        .apply(lambda row: row.sum(), axis=1)
    )
    df = pd.DataFrame(df, columns=["vals"])
    df_ops = pd.DataFrame(operations, columns=["op"]).reset_index()

    df["vals"] = df.sum(axis=1)
    df["is_empty"] = df["vals"].apply(lambda x: 1 if x.strip() == "" else 0)
    df["index"] = df["is_empty"].cumsum()
    df = df.loc[df["is_empty"] == 0]

    df_grouped = df.groupby("index")["vals"].agg(list).reset_index()

    df_result = pd.merge(
        df_grouped,
        df_ops,
        on="index"
    ).drop(columns=["index"])
    
    df_vals_expanded = df_result["vals"].apply(pd.Series)
    df_result = pd.concat([df_result, df_vals_expanded], axis=1).drop(columns=["vals"])
    val_cols = [c for c in df_result.columns if isinstance(c, int)]

    df_result[val_cols] = df_result[val_cols].apply(pd.to_numeric, errors="coerce").astype("float")
    df_result["result_mult"] = df_result.loc[df_result["op"] == "*"][val_cols].prod(axis=1)
    df_result["result_sum"] = df_result.loc[df_result["op"] == "+"][val_cols].sum(axis=1)
    df_result["result"] = df_result["result_sum"].fillna(df_result["result_mult"])

    return int(df_result["result"].sum())

# %%
p1(parse_data_p1("data/data1.txt"))
# %%
p2("data/data1.txt")
# %%
