from django.test import TestCase
from carRental.models import Customer, Employee, Manager, Complaint
from django.contrib.auth.models import User
from decimal import *
# Create your tests here.

# Testing Customers
class CustomerTestCase(TestCase):
    def setUp(self):
        user_test_1 = User.objects.create_user(username='user_test_1', password='foobar1')
        user_test_2 = User.objects.create_user(username='user_test_2', password='foobar2')
        user_test_3 = User.objects.create_user(username='user_test_3', password='foobar3')
        user_test_4 = User.objects.create_user(username='user_test_4', password='foobar4')
        user_test_5 = User.objects.create_user(username='user_test_5', password='foobar5')
        Customer.objects.create(user=user_test_1)
        Customer.objects.create(user=user_test_2)
        Customer.objects.create(user=user_test_3)
        Customer.objects.create(user=user_test_4)
        Customer.objects.create(user=user_test_5)

    def test_addMoney_function(self):
        customer1 = Customer.objects.get(user__username='user_test_1')
        customer1.addMoney(10)
        self.assertEqual(customer1.balance, 10)
        customer2 = Customer.objects.get(user__username='user_test_2')
        customer2.addMoney(1000000)
        self.assertEqual(customer2.balance, 1000000)
        customer3 = Customer.objects.get(user__username='user_test_3')
        customer3.addMoney(100)
        self.assertEqual(customer3.balance, 100)
        customer4 = Customer.objects.get(user__username='user_test_4')
        customer4.addMoney(5)
        self.assertEqual(customer4.balance, 5)
        customer5 = Customer.objects.get(user__username='user_test_5')
        customer5.addMoney(0)
        self.assertEqual(customer5.balance, 0)

    def test_complaints(self):
        user1 = User.objects.get(username='user_test_1')
        user2 = User.objects.get(username='user_test_2')
        user3 = User.objects.get(username='user_test_3')
        user4 = User.objects.get(username='user_test_4')
        user5 = User.objects.get(username='user_test_5')
        complaint1 = Complaint.objects.create(user=user1,
                                              description="Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                                                          " sed do eiusmod tempor incididunt ut labore et dolore "
                                                          "magna aliqua. Euismod quis viverra nibh cras pulvinar "
                                                          "mattis nunc. Urna duis convallis convallis tellus id "
                                                          "interdum velit laoreet. Volutpat blandit aliquam etiam "
                                                          "erat velit scelerisque in. Posuere urna nec tincidunt "
                                                          "praesent semper feugiat nibh.")
        complaint2 = Complaint.objects.create(user=user2,
                                              description="I'm upset.")
        complaint3 = Complaint.objects.create(user=user3,
                                              description="")
        complaint4 = Complaint.objects.create(user=user4,
                                              description="324985793824758937425807")
        complaint5 = Complaint.objects.create(user=user5,
                                              description="5.55")
        self.assertIsInstance(complaint1.description, str)
        self.assertIsInstance(complaint2.description, str)
        self.assertIsInstance(complaint3.description, str)
        self.assertIsInstance(complaint4.description, str)
        self.assertIsInstance(complaint5.description, str)