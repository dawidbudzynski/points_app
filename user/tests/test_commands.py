from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase


class CommandTests(TestCase):

    def test_create_users_from_command_successful(self):
        """Test creating a new user using import_users command is successful"""

        self.assertEqual(get_user_model().objects.all().count(), 0)
        call_command('import_users_data', 'temp/test_users.csv')
        # users created successfully
        self.assertEqual(get_user_model().objects.all().count(), 9)
        # user created with correct balance
        self.assertEqual(get_user_model().objects.get(email='lkennsley1@ehow.com').balance, 658)
        # user created with correct balance and rewarded 20 point for referring other user
        self.assertEqual(get_user_model().objects.get(email='rralphsks@ibm.com').balance, 527 + 20)
