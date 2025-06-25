import warnings
from django.core.management.base import BaseCommand
import csv
from blog.models import Job
warnings.simplefilter(action='ignore', category=RuntimeWarning)

class Command(BaseCommand):
    help = 'Imports job listings from a specified CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        jobs = []
        count = 0

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'posted time' in row:
                    row['date'] = Job.parse_relative_date(row['posted time'])
                job = Job.create_from_csv_row(row)
                if job:
                    jobs.append(job)
                else:
                    count += 1
        print(f"Skipped {count} invalid rows.")

        Job.objects.bulk_create(jobs, batch_size=100)
        self.stdout.write(self.style.SUCCESS(f'Bulk imported {len(jobs)} jobs into default from {csv_file_path}'))

