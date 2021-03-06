import csv

from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = 'Imports users from csv file'

    def add_arguments(self, parser):
        parser.add_argument('source_file', type=str, nargs='?')

    def handle(self, *args, **options):
        """
        Script reads user data from csv file and creates new User objects in database.
        Objects are created in bulk (1000 in batch) for performance improvement.
        """
        source_file = options.get('source_file', None)

        self.create_new_users(source_file)
        self.add_points_to_referrers(source_file)

    @staticmethod
    def create_new_users(source_file):
        """Saves new users to database"""
        print(u'Creating objects list...')
        bulk_object_list = []
        with open(source_file, "r") as f:
            rows = csv.reader(f, delimiter=',')
            next(rows, None)  # skip header
            for row in rows:
                id = row[0]
                first_name = row[1]
                last_name = row[2]
                email = row[3]
                balance = row[5]
                bulk_object_list.append(
                    User(id=id, first_name=first_name, last_name=last_name, email=email, balance=balance)
                )
            print(u'Saving objects to database...')
            User.objects.bulk_create(bulk_object_list, batch_size=1000)
            print(u'All objects saved to database')

    @staticmethod
    def add_points_to_referrers(source_file):
        """Iterates over file rows and adds 20 point to users who referred new users"""
        with open(source_file, "r") as f:
            rows = csv.reader(f, delimiter=',')
            next(rows, None)  # skip header
            for row in rows:
                referrer_email = row[4]
                if referrer_email:
                    referrer = User.objects.filter(email=referrer_email).first()
                    if referrer:
                        referrer.balance += 20
                        referrer.save()
                        print(f"Balance of {referrer_email} increased by 20 points")
                    else:
                        print(f"User with email {referrer_email} doesn't exist")
