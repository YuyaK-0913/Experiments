from datetime import date
import pandas as pd
import numpy as np
from itertools import product

dates = pd.date_range(start="2020-01-01", end="2022-12-31")
# print(dates)
times = pd.date_range(start="13:00", end="23:00", freq="10T").time
# print(times)
stores = np.arange(0, 101, 10)
# print(stores)

# Create all combinations of date, time, store
combinations = list(product(dates, times, stores))
# print(
#     len(combinations) == len(dates) * len(times) * len(stores)
#     )


# Create Sales DataFrame
sales = np.random.randint(0, 31, len(combinations))
sales_df = pd.DataFrame(combinations, columns=["date", "time", "store"])
sales_df["sales"] = sales
sales_df.to_csv("sales.csv", index=False)

# Create Area DataFrame
area1 = np.random.randint(0, 101, len(dates))
area2 = np.random.randint(0, 101, len(dates))
area3 = np.random.randint(0, 101, len(dates))
area_df = pd.DataFrame(
    list(zip(dates, area1, area2, area3)),
    columns=["date", "area1", "area2", "area3"]
    )
area_df.to_csv("area.csv", index=False)
