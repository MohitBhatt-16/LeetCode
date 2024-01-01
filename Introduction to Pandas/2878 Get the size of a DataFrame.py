import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    ls=[]
    for i in range(len(players.shape)):
        ls.append(players.shape[i])

    return ls