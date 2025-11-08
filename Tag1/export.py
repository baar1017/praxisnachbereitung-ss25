import pandas as pd
from datetime import datetime

xlsx_path = r"C:\LocalThingsOfLife\HKA\Praxisnachbereitung\the_repo\praxisnachbereitung-ss25\Tag1\Tag1.xlsx"
sheet = "Ausleihen"

out_path = f"gesamttabelle_{datetime.now():%Y-%m-%d}.csv"

df = pd.read_excel(xlsx_path, sheet_name=sheet)
df.columns = [c.strip() for c in df.columns]
df.to_csv(out_path, index=False, sep=";", encoding="utf-8")
print(f"Export of -> {out_path}")