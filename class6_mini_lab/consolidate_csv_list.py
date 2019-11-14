import pandas as pd
import os
data_root = '/Users/pankaj/dev/data/nifty50'
import datetime as dt
w = os.walk(data_root)
in_files = set(['nifty50_mcwb.csv', 'niftymcwb.csv'])
consolidated_df = pd.DataFrame()
for a, b ,c  in w:
    files_to_read = set(c).intersection(in_files)
    if len(files_to_read)>0:
        for csv in files_to_read:
            if csv.endswith('.csv'):
                csv_file = os.path.join(a, csv)
                print('processing {} '.format(csv_file))
                try:
                    df = pd.read_csv(csv_file, header=None)
                except:
                    print('error while reading {}'.format(csv_file))
                    continue

                try:
                    rp_date=dt.datetime.strptime(df[0][0].split(':')[1].strip(), '%B %Y') if len(df[0][0].split(':'))>1 \
                        else dt.datetime.strptime(csv_file.split(os.path.sep)[6], '%b%y')
                except:
                    rp_date=dt.datetime.strptime(df[0][0].split(':')[1].strip(), '%b %Y')

                df = df[df[0].isin([str(a) for a in range(1, 51)])]
                df['report_date'] = rp_date
                consolidated_df = consolidated_df.append(df)
                print('done for date {}'.format(rp_date))

consolidated_df.to_csv(os.path.join(data_root, 'nifty_fifty_companies.csv'))

print('all_done')
