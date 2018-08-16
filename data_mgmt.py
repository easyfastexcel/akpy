import pandas as pd

from akpy.time_mgmt import *
from akpy.stnd_vars import StandardMessages


msg_contactak = StandardMessages.msg_contactak


def convert_pd_column_to_datetime64(df, list_pd_columns):
    list_incovertibles = []
    if len(list_pd_columns) > 0:
        # for c, d in zip(list_pd_columns, df[list_pd_columns].dtypes):
        for c in list_pd_columns:
            try:
                df[c] = pd.to_datetime(df[c])
            except TypeError as e:
                print(e)
                print('[ERROR] an error encountered during execution of '
                      '"def convert_pd_column_to_datetime64" for column:', c)
                sys.exit(msg_contactak)

            if df[c].dtype != 'datetime64[ns]':
                print(c)
                list_incovertibles.append(c)
    else:
        sys.exit('[ERROR (def convert_to_datetime64)] no columns were passed through in "list_pd_columns"')

    if len(list_incovertibles) > 0:
        sys.exit(
            '[ERROR (def convert_to_datetime64)] the following column(s) '
            'could not be converted to dtype(datetime64[ns]): ' + ", ".join(
                list_incovertibles))
    else:
        print('[', time_stamp(), ']', 'The columns', ", ".join(list_pd_columns),
              'are now converted to dtype(datetime64[ns])')

        return df


def convert_pd_column_to_str(df, list_pd_columns):
    list_incovertibles = []
    if len(list_pd_columns) > 0:
        # for c, d in zip(list_pd_columns, df[list_pd_columns].dtypes):
        for c in list_pd_columns:
            try:
                df[c] = df[c].astype(str)
            except TypeError as e:
                print(e)
                print('[ERROR] an error encountered during execution of '
                      '"def convert_pd_column_to_str" for column:', c)
                sys.exit(msg_contactak)

            if df[c].dtype != 'object':
                print(c)
                list_incovertibles.append(c)
    else:
        sys.exit('[ERROR (def convert_pd_column_to_str)] no columns were passed through in "list_pd_columns"')

    if len(list_incovertibles) > 0:
        sys.exit(
            '[ERROR (def convert_pd_column_to_str)] the following column(s) '
            'could not be converted to dtype(object): ' + ", ".join(
                list_incovertibles))
    else:
        print('[', time_stamp(), ']', 'The columns', ", ".join(list_pd_columns), 'are now converted to dtype(object)')

        return df
