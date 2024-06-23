# -*- coding: utf-8 -*-

import datetime as dt
from dateutil.relativedelta import relativedelta
def get_periods(start_date, end_date, months_per_period):
    periods = []
    current_date = start_date

    while current_date <= end_date:
        # Calcular la fecha de finalización del periodo
        period_end = current_date + relativedelta(months=months_per_period) - dt.timedelta(days=1)

        # Asegurarse de que el periodo no sobrepase la fecha final
        if period_end > end_date:
            period_end = end_date

        periods.append((current_date, period_end))

        # Mover la fecha al principio del siguiente periodo
        current_date = period_end + dt.timedelta(days=1)

    return periods

# start_date = dt.date(2000, 1, 1)
# end_date = dt.date(2023, 12, 31)
# months_per_period = 3

# periods = get_periods(start_date, end_date, months_per_period)

# for period in periods:
#     print(period[0], period[1])
    # print(period)

# for i, (period_start, period_end) in enumerate(periods):
#     print(f"Periodo {i+1}: {period_start} - {period_end}")

