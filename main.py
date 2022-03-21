import pandas as pd
import time
import table

def main():

    LEAs = set()
    schools = set()
    rev_funds = set()
    expense_funds = set()

    db = table.Table("main")

    # import each excel sheet

    rev = table.Table("revenue")
    rev_filename = "revenue/revenuedump_csv.csv"
    df_rev = pd.read_csv(rev_filename)

    df_rev.drop('Submitted Date', axis=1, inplace=True)
    df_rev.drop('Certified Date', axis=1, inplace=True)
    df_rev.drop('Revenue Source Two Digit', axis=1, inplace=True)

    df_rev.rename(columns={'District Number': 'LEA_num', 'District Name': 'LEA', 'Location School Id':
                           'school_id', 'Location School Number': 'school_num', 'Location School': 'school_id',
                           'Fund Code': 'fund_code', 'Revenue Code': 'rev_code', 'Program Code': 'program_code',
                           'Amount': 'rev_amt', 'Year': 'year'}, inplace=True)

    df_rev['fund_id'] = df_rev['fund_code'].astype(str) + '_' + df_rev['rev_code'].astype(str) + '_' + df_rev['program_code'].astype(str)


    rev.set_df(df_rev)

    LEAs.update(df_rev['LEA_num'].tolist())
    schools.update(df_rev['school_num'].tolist())

    print(LEAs)
    print(schools)

    # analysis
    # for each unique district (school_id), sum amount of programs by year
    fund_amts = df_rev.groupby(['school_id', 'year'])['fund_id'].nunique()
    print(fund_amts)


main()