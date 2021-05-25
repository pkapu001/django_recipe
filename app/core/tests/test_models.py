from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating a user with as email"""
        email = 'Dragon007@gmail.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test email for the new user is normalized"""
        email = 'Dragon007@GMAIL.COM'
        normalised_email = 'Dragon007@gmail.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='testpass'
        )
        self.assertEqual(user.email, normalised_email)

    def test_newuser_invalid_email(self):
        """ test using invalid email or empty email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')
            get_user_model().objects.create_user('dragon', 'testpass')

    def test_create_new_super_user(self):
        """ test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'dragon007@gmail.com',
            'testpass'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
