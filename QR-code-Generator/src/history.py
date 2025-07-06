import csv
from datetime import datetime

def log_history(data, filename):
    with open("qr_history.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now().isoformat(), data, filename])