from django.core.management.base import BaseCommand
import csv
from listings.models import Realtor

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = "realtor_detail.csv"

        Realtor.objects.all().delete()

        with open(file_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                Realtor.objects.create(
                    name=row["Name"],
                    phone=row["Phone"],
                    email=row["Email"],
                    locality=row["Locality"],
                    district=row["District"],
                    state=row["State"]
                )

        print("✅ Realtors Imported Successfully")