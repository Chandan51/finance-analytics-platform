import pandas as pd
import numpy as np

print("Environment working successfully")

data = {
    "stock": ["AAPL", "MSFT", "SAP"],
    "price": [210, 430, 265]
}

df = pd.DataFrame(data)

print(df)