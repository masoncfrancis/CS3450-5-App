from django.test import TestCase
from carRental.models import Customer, Employee, Manager, Complaint
from django.contrib.auth.models import User
from decimal import *
# Create your tests here.

# Testing Accounts For 5 Users
class AccountTestCase(TestCase):
    def setUp(self):
        # Setting Up Data Base For Account Tests
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


    # Testing addMoney() function for Customers Adding Funds To Account
    def test_addMoney_function_1(self):
        customer1 = Customer.objects.get(user__username='user_test_1')
        customer1.addMoney(10)
        self.assertEqual(customer1.balance, 10)

    def test_addMoney_function_2(self):
        customer2 = Customer.objects.get(user__username='user_test_2')
        customer2.addMoney(1000000)
        self.assertEqual(customer2.balance, 1000000)

    def test_addMoney_function_3(self):
        customer3 = Customer.objects.get(user__username='user_test_3')
        customer3.addMoney(100)
        self.assertEqual(customer3.balance, 100)

    def test_addMoney_function_4(self):
        customer4 = Customer.objects.get(user__username='user_test_4')
        customer4.addMoney(5)
        self.assertEqual(customer4.balance, 5)

    def test_addMoney_function_5(self):
        customer5 = Customer.objects.get(user__username='user_test_5')
        customer5.addMoney(0)
        self.assertEqual(customer5.balance, 0)


    # Testing Complaint Description Type For Customers
    def test_complaint_type_1(self):
        user1 = User.objects.get(username='user_test_1')
        complaint1 = Complaint.objects.create(user=user1,
                                              description="Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                                                          " sed do eiusmod tempor incididunt ut labore et dolore "
                                                          "magna aliqua. Euismod quis viverra nibh cras pulvinar "
                                                          "mattis nunc. Urna duis convallis convallis tellus id "
                                                          "interdum velit laoreet. Volutpat blandit aliquam etiam "
                                                          "erat velit scelerisque in. Posuere urna nec tincidunt "
                                                          "praesent semper feugiat nibh.")
        self.assertIsInstance(complaint1.description, str)

    def test_complaint_type_2(self):
        user2 = User.objects.get(username='user_test_2')
        complaint2 = Complaint.objects.create(user=user2,
                                              description="I'm upset.")
        self.assertIsInstance(complaint2.description, str)

    def test_complaint_type_3(self):
        user3 = User.objects.get(username='user_test_3')
        complaint3 = Complaint.objects.create(user=user3,
                                              description="")
        self.assertIsInstance(complaint3.description, str)

    def test_complaint_type_4(self):
        user4 = User.objects.get(username='user_test_4')
        complaint4 = Complaint.objects.create(user=user4,
                                              description="324985793824758937425807")
        self.assertIsInstance(complaint4.description, str)

    def test_complaint_type_5(self):
        user5 = User.objects.get(username='user_test_5')
        complaint5 = Complaint.objects.create(user=user5,
                                              description="5.55")
        self.assertIsInstance(complaint5.description, str)


    # Testing Account Field Changes
    def test_first_name_change(self):
        user1 = User.objects.get(username='user_test_1')
        user2 = User.objects.get(username='user_test_2')
        user3 = User.objects.get(username='user_test_3')
        user4 = User.objects.get(username='user_test_4')
        user5 = User.objects.get(username='user_test_5')
        user1.first_name = "foo1"
        user2.first_name = "foo2"
        user3.first_name = "foo3"
        user4.first_name = "foo4"
        user5.first_name = "foo5"
        user1.save()
        user2.save()
        user3.save()
        user4.save()
        user5.save()
        self.assertEqual(user1.first_name, "foo1")
        self.assertEqual(user2.first_name, "foo2")
        self.assertEqual(user3.first_name, "foo3")
        self.assertEqual(user4.first_name, "foo4")
        self.assertEqual(user5.first_name, "foo5")

    def test_last_name_change(self):
        user1 = User.objects.get(username='user_test_1')
        user2 = User.objects.get(username='user_test_2')
        user3 = User.objects.get(username='user_test_3')
        user4 = User.objects.get(username='user_test_4')
        user5 = User.objects.get(username='user_test_5')
        user1.last_name = "bar1"
        user2.last_name = "bar2"
        user3.last_name = "bar3"
        user4.last_name = "bar4"
        user5.last_name = "bar5"
        user1.save()
        user2.save()
        user3.save()
        user4.save()
        user5.save()
        self.assertEqual(user1.last_name, "bar1")
        self.assertEqual(user2.last_name, "bar2")
        self.assertEqual(user3.last_name, "bar3")
        self.assertEqual(user4.last_name, "bar4")
        self.assertEqual(user5.last_name, "bar5")

    def test_email_change(self):
        user1 = User.objects.get(username='user_test_1')
        user2 = User.objects.get(username='user_test_2')
        user3 = User.objects.get(username='user_test_3')
        user4 = User.objects.get(username='user_test_4')
        user5 = User.objects.get(username='user_test_5')
        user1.email = "email1"
        user2.email = "email2"
        user3.email = "email3"
        user4.email = "email4"
        user5.email = "email5"
        user1.save()
        user2.save()
        user3.save()
        user4.save()
        user5.save()
        self.assertEqual(user1.email, "email1")
        self.assertEqual(user2.email, "email2")
        self.assertEqual(user3.email, "email3")
        self.assertEqual(user4.email, "email4")
        self.assertEqual(user5.email, "email5")