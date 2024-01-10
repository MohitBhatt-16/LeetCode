import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        frame=report,
        id_vars=["product"],
        value_vars=[f"quarter_{i}" for i in range(1, 4+1)],
        var_name="quarter",
        value_name="sales",
    )
 
    