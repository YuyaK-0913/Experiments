from typing import Required
import pandas as pd
import click

@click.command()
@click.option('--start_date', required=True, help='Start date for the data extraction')
@click.option('--end_date', required=True, help='End date for the data extraction')
def main(start_date: str, end_date: str):
    input_dir = '/mnt/c/Users/kuniy/OneDrive/デスクトップ/Experiments/MLsystem/dataset/'
    
    # print('Start date:', start_date)
    # print('End date:', end_date)

    # Loading sale.csv
    sales_df = pd.read_csv(input_dir+'sales.csv')
    # sales_df['date'] = pd.to_datetime(input_dir+sales_df['date'])
    
    # Loading area_df.csv
    area_df = pd.read_csv(input_dir+'area.csv')

    # Extracting from the date column
    sales_df = sales_df[(sales_df['date'] >= start_date) & (sales_df['date'] <= end_date)]
    area_df = area_df[(area_df['date'] >= start_date) & (area_df['date'] <= end_date)]

    # print(sales_df)
    # print(area_df)


if __name__ == '__main__':
    main()

# Run the script
# python ingest.py --start_date 2020-01-01 --end_date 2020-01-31
