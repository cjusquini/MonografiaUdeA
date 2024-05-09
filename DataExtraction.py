import datetime as dt
import pydataxm
from pydataxm.pydataxm import ReadDB
import pandas as pd
import pathlib
import os    
from periods import get_periods
import time
abspath = pathlib.Path.cwd()
start_date = dt.date(2015, 1, 1)
# end_date = dt.date(2000,1,31)
end_date = dt.date(2019, 12, 31)

months_per_period = 3
periods = get_periods(start_date, end_date, months_per_period)
metricas = [
    ["AporEner","Sistema"],
    ["CompBolsNaciEner", "Sistema"],
    ["CompContEner", "Sistema"],
    ["DemaSIN","Sistema"],
    ["DispoDeclarada", "Recurso"],
    ["DispoReal", "Recurso"],
    ["Gene", "Sistema"],
    ["PrecBolsNaci", "Sistema"],
    ["PrecOferDesp", "Recurso"],
    ["VentBolsNaciEner", "Sistema"],
    ["VentContEner", "Sistema"],
    ["VoluUtilDiarEner", "Sistema"]
]


if not os.path.exists(os.path.join(abspath, "MonografiaUdeA", "datasets")):
    os.makedirs(os.path.join(abspath, "MonografiaUdeA", "datasets"))


for metrica in metricas:
    consult = ReadDB()
    df = pd.DataFrame()
    print(metrica)
    # metrica = _reg
    for period in periods:
        print(period[0], period[1])        
        df_cons = consult.request_data(metrica[0], metrica[1], period[0], period[1])     
        df = pd.concat([df, df_cons])
        time.sleep(2)

    df.to_csv(os.path.join(abspath, "MonografiaUdeA", "datasets", f"{metrica[0]}.csv"), index=False) 