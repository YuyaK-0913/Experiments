import pandas as pd
import click

@click.command()
@click.option('--time', required=True, help='Time for the data extraction')
@click.option('--store', required=True, help='Store for the data extraction')
def main(time: str, store: int):    
    print('time:', time)
    print('store:', store)

    
if __name__ == '__main__':
    main()

# Run the script
# python preprocess.py --time 15:00:00 --store 10