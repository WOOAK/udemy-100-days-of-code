import requests
from bs4 import BeautifulSoup
import pandas as pd

records = []

for current_page in range(34):
    endpoint = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{current_page + 1}"
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    rows = soup.select("table.data-table tbody tr")
    for row in rows:
        cells = row.select("span.data-table__value")
        record = {
            "Undergraduate Major": cells[1].getText(),
            "Starting Median Salary": float(cells[3].getText().strip("$").replace(",", "")),
            "Mid-Career Median Salary": float(cells[4].getText().strip("$").replace(",", "")),
        }
        records.append(record)

pd.DataFrame(records).to_csv("salaries_by_college_major_updated.csv", index=False)