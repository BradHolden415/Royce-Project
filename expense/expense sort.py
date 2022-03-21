import pandas as pd
import time

start = time.perf_counter()
filename = "annual_expend.xlsx"
dfs = pd.read_excel(filename, engine='openpyxl', sheet_name=None)
funds = [10, 20, 21, 23, 26, 31, 32, 40, 49, 50, "ALL"]
fund_index = 0
df_new = pd.DataFrame(columns=['LEA', 'fund', 'function', 'category', 'amount', 'year'])
for df in dfs:
    df = dfs[df]

    # find height and width
    x, y, height, width = 0, 0, 0, 0
    found = False

    # loop through first column until "GRAND TOTAL" is found, signaling the bottom
    while not found:
        curr = df.iloc[y, x]
        if str(curr).lower() == "grand total":
            # found height
            height = y
            found = True

            # find width by iterating until IndexError is found
            x += 2
            x_found = False
            while not x_found:
                x += 1
                try:
                    curr = df.iloc[y, x]
                except IndexError:
                    width = x
                    x_found = True
                    break
            break
        else:
            y += 1

    fund = funds[fund_index]

    fiscal_year = df.iloc[0, 1]
    end = False
    non_null_function = "unfound"
    non_null_category = "unfound"
    x, y = 1, 1
    while x < (width - 1):
        y = 2
        x += 1
        function = df.iloc[y-1, x]
        if pd.notna(function):
            non_null_function = df.iloc[y, x]
        else:
            function = non_null_function

        category = df.iloc[y + 1, x]
        if pd.notna(category):
            non_null_category = df.iloc[y + 2, x]
        else:
            category = non_null_category

        y += 4
        LEA_NUM = df.iloc[y, 0]
        for y in range(height):
            LEA_NUM = df.iloc[y, 0]
            LEA = df.iloc[y, 1]
            if pd.notna(LEA):

                amount = df.iloc[y, x]
                row = {'LEA': LEA, 'fund': fund, 'function': function, 'category': category, 'amount': amount, 'year': fiscal_year}
                df_new = df_new.append(row, ignore_index=True)
    fund_index += 1

print(df_new.head())
end = time.perf_counter()
df_new.to_csv('PANDAS_EXPORT.csv')

print(start - end)


