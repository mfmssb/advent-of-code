filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

# ## Intermediate Steps 1

import pandas as pd


def preprocess_data(data_in, sort_columns=True):
    d = data_in.split("\n")
    
    left, right = [], []
    for pair in d:
        pair_list = pair.split('   ')
        left.append(pair_list[0])
        right.append(pair_list[1])
    
    left = pd.DataFrame(left, columns=['left'], dtype='float')
    right = pd.DataFrame(right, columns=['right'], dtype='float')

    if sort_columns:
        left  = left.sort_values('left').reset_index(drop=True)
        right = right.sort_values('right').reset_index(drop=True)
    
    return pd.concat([left, right], axis=1)


def calculate_diff(df):
    df['diff'] = abs(df['left'] - df['right'])
    return df


# ## Solution 1

# # %%timeit
df = preprocess_data(data[1])
calculate_diff(df)
ans = df['diff'].sum()

print(int(ans))


# # Problem 2

# ## Intermediate Steps 1

def calculate_score(df):
    df['in_right'] = df['left'].isin(df['right'])

    df_agg = df.groupby('left').agg(
        num_times_in_right=('in_right', 'sum')
    ).reset_index()
    
    df_agg['score'] = df_agg['left'] * df_agg['num_times_in_right'].apply(lambda x: x**2)
    
    return df_agg['score'].sum()



data[0]

df = preprocess_data(data[0], False)

df

unique_lefts_in_right = pd.DataFrame(
    df[df['left']
        .isin(df['right'])]['left']
        .unique(),
    columns=['unique_left']
)

right_counts = df['right'].value_counts().reset_index()

right_counts

final = pd.merge(
    unique_lefts_in_right,
    right_counts,
    left_on='unique_left',
    right_on='right',
    how='inner'
).drop(columns='right')

final['score'] = final['unique_left'] * final['count'].apply(lambda x: x**2)

final







# %%timeit
df = preprocess_data(data[1])
ans = calculate_score(df)

ans = calculate_score(df)

# ## Solution 2

# 2193494

print(int(ans))


