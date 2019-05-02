import datetime
from datetime import timedelta, date


def date_range(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)

        
def last_and_next_dates(list_of_dates, cutoff_date=datetime.datetime.now()):
    list_of_dates = [d for d in list_of_dates if d != '.']
    i=0
    list_belowcut = []
    list_abovecut = []
    for d in sorted(list(set(list_of_dates))):
        if d < cutoff_date:
            list_belowcut.append(d)
        else:
            list_abovecut.append(d)
            
    imv_last = max(list_belowcut) if list_belowcut else None
    imv_next = min(list_abovecut) if list_abovecut else None

    # print('cutoff date:', cutoff_date,
    #       '\nlast imv date:', imv_last, 
    #       '\nnext imv date:', imv_next)
    
    return imv_last, imv_next


if __name__ == '__main__':
    pass
    # start_dt = date(2015, 12, 20)
    # end_dt = date(2016, 1, 11)
    # for dt in date_range(start_dt, end_dt):
    #     print(dt.strftime("%Y-%m-%d"))
