import pandas as pd
import time

def main():

    LEAs = set()
    schools = set()
    rev_funds = set()
    expense_funds = set()

    # import each excel sheet

    rev_filename = "revenue/revenue.csv"
    df_rev = pd.read_csv(rev_filename)

    df_rev.rename(columns={'District Number': 'LEA_num', 'District Name': 'LEA', 'Location School Id':
                           'school_id', 'Location School Number': 'school_num', 'Location Name': 'school',
                           'Fund Code': 'fund_code', 'Revenue Code': 'rev_code', 'Program Code': 'program_code',
                           'Amount': 'rev_amt', 'Year': 'year'}, inplace=True)
    df_rev.dropna(inplace=True)

    df_rev['fund_code'] = df_rev['fund_code'].astype('str')
    df_rev['rev_code'] = df_rev['rev_code'].astype('str')
    df_rev['program_code'] = df_rev['program_code'].astype('str')

    # create a list of all funds
    print(df_rev['rev_code'].nunique())
    rev_funds.update(set(df_rev['rev_code'].tolist()))
    print(rev_funds)
    LEAs.update(set(df_rev['LEA']))

    # wide format by revenue code
    df_rev.groupby(['LEA', 'school', 'year', 'rev_code'])['rev_amt'].sum().unstack('rev_code').to_csv(
        "rev_group_by_1.csv")

    # wide format by revenue code and fund code
    df_rev['fund_id'] = df_rev['fund_code'] + "_" + df_rev['rev_code']
    df_rev.groupby(['LEA', 'school', 'year', 'fund_id'])['rev_amt'].sum().unstack('fund_id').to_csv(
        "rev_group_by_2.csv")

    # wide format by all subcategories (big!)
    df_rev['fund_id'] = df_rev['fund_code'] + "_" + df_rev['rev_code'] + df_rev['program_code']
    df_rev.groupby(['LEA', 'school', 'year', 'fund_id'])['rev_amt'].sum().unstack('fund_id').to_csv(
        "rev_group_by_3.csv")

    exp_filename = "expense/expense.csv"
    df_exp = pd.read_csv(exp_filename)

    df_exp.rename(columns={'District Number': 'LEA_num', 'District Name': 'LEA', 'Location School Id':
        'school_id', 'Location School Number': 'school_num', 'Location Name': 'school',
                           'Fund Code': 'fund_code', 'Function Code': 'exp_code', 'Program Code': 'program_code',
                           'Amount': 'exp_amt', 'Year': 'year'}, inplace=True)

    df_exp.dropna(inplace=True)

    df_exp['fund_code'] = df_exp['fund_code'].astype('str')
    df_exp['exp_code'] = df_exp['exp_code'].astype('str')
    df_exp['program_code'] = df_exp['program_code'].astype('str')

    # create a list of all funds
    print(df_exp['exp_code'].nunique())
    expense_funds.update(set(df_exp['exp_code'].tolist()))
    print(expense_funds)
    LEAs.update(set(df_exp['LEA']))

    # wide format by revenue code
    df_exp.groupby(['LEA', 'school', 'year', 'exp_code'])['exp_amt'].sum().unstack('exp_code').to_csv(
        "exp_group_by_1.csv")

    # wide format by revenue code and fund code
    df_exp['fund_id'] = df_exp['fund_code'] + "_" + df_exp['exp_code']
    df_exp.groupby(['LEA', 'school', 'year', 'fund_id'])['exp_amt'].sum().unstack('fund_id').to_csv(
        "exp_group_by_2.csv")

    # wide format by all subcategories (big!)
    df_exp['fund_id'] = df_exp['fund_code'] + "_" + df_exp['exp_code'] + df_exp['program_code']
    df_exp.groupby(['LEA', 'school', 'year', 'fund_id'])['exp_amt'].sum().unstack('fund_id').to_csv(
        "exp_group_by_3.csv")

    df_merge = df_rev.merge(df_exp, how='left', on=['LEA', 'school', 'year'])
    df_merge.to_csv('merge.csv')



    #df_rev = df_rev.pivot(index="school", columns="rev_code", values="rev_amt")

    # loop through data frame, sorting data


    # for c in df_rev.columns:
    #     print(c)

    # df_rev['dummy_index'] = df_rev.index
    # df_rev = df_rev.pivot(index='dummy_index', columns=['fund_id'], values="rev_amt")
    # print(df_rev.head())

    # reformat RISE data
    # df_rise = pd.read_csv('proficiency/rise/rise_total.csv')
    # df_rise.rename(columns={'District ID': 'school_id'}, inplace=True)
    # df_rise.drop(columns={'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9',
    #    'Unnamed: 10', 'Unnamed: 11'}, inplace=True)
    #
    # merge = pd.merge(how="outer", on="school_id", left=df_rev, right=df_rise)
    # merge.to_csv('merge.csv')
    # # combine on LEA
    #
    #
    # LEAs.update(df_rev['LEA_num'].tolist())
    # schools.update(df_rev['school_num'].tolist())

    # analysis
    # for each unique district (school_id), sum amount of programs by year
    # fund_amts = df_rev.groupby(['school_id', 'year'])['fund_id'].nunique()
    # print(fund_amts)


main()