def display(df):
    import pandas as pd
    pd.options.display.max_columns = None
    pd.options.display.max_rows = False
    return(df.limit(1000).toPandas())
