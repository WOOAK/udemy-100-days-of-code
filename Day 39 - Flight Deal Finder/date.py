import datetime as dt

SIX_MONTHS_DAY = dt.timedelta(days=180)
ONE_DAY = dt.timedelta(days=1)

class Date:
    def __init__(self):
        super().__init__()
    def get_date(self):
        self.today = dt.datetime.now().date()
        self.start_date = self.today + ONE_DAY
        self.end_date = self.today + SIX_MONTHS_DAY

        return self.start_date,self.end_date
