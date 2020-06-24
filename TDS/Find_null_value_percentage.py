def cal_per_missing_values(df):
    '''
    This funtion is used to calculate the total percentage 
    of missing values in each column of the dataframe'''

    # Get the total rows in the dataframe
    l_total_rows = df.shape[0]

    # Get the total columns in the dataframe
    l_total_cols = df.shape[1]

    # get the series of non null rows using the count method
    l_non_null_rows_series = df.count()

    # create a dictionary that will store the details
    l_df_dic = {
        'Column_Name': [],
        'Total_Rows': [l_total_rows] * l_total_cols,
        'Missing_rows': [],
        'Null_Percentage': [],
        }

    # iterate through each row and calculate the percentage value.
    for index in l_non_null_rows_series.index:
        l_null_rows = l_total_rows - l_non_null_rows_series[index]

        l_null_per = round(l_null_rows / l_total_rows * 100, 2)

        l_df_dic['Column_Name'].append(index)
        l_df_dic['Null_Percentage'].append(l_null_per)
        l_df_dic['Missing_rows'].append(l_null_rows)

    # sort the dataframe based on highest % of missing values

    temp_df = pd.DataFrame(l_df_dic).sort_values('Null_Percentage',
            ascending=False).reset_index().drop(columns=['index'])

    return temp_df
