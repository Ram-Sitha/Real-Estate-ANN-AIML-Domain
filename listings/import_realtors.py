import csv
from listings.models import Realtor

def run():
    with open("realtor_details.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            Realtor.objects.create(
                name=row["Name"],
                email=row["Email"],
                locality=row["Locality"],
                district=row["District"],
                state=row["State"]
            )

    print("✅ Realtors imported successfully")