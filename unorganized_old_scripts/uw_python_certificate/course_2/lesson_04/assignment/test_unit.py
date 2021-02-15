"""Module for testing individual functions of basic operations"""

import unittest
from unittest import TestCase

import customer_model as cm
import basic_operations as bo


class BasicOperationsTest(TestCase):
    """Testing basic operations"""

    @classmethod
    def setUp(cls):
        """Setup database"""
        cm.DATABASE.drop_tables([cm.Customer])
        cm.DATABASE.create_tables([cm.Customer])

    @classmethod
    def tearDown(cls):
        """Close database"""
        cm.DATABASE.close()

    def test_add_customer(self):
        """Test adding a new customer"""
        bo.add_customer(100, 'Peter', 'Parker',
                        '135 W. 50th Street, New York City, NY 10011',
                        '212-576-4000', 'peter.parker@marvel.com',
                        True, 1000)
        bo.add_customer(200, 'Iron', 'Man',
                        '17801 International Blvd, Seattle, WA 98101',
                        '206-787-5388', 'iron.man@gmail.com',
                        True, 5000)
        bo.add_customer(300, 'Ramkumar', 'Rajanbabu',
                        '7525 166th Ave NE, Redmond, WA 98052',
                        '425-556-2900', 'ram.kumar@gmail.com',
                        False, 7078)

        cus_1 = cm.Customer.get(cm.Customer.customer_id == 100)
        self.assertEqual(cus_1.customer_id, 100)
        self.assertEqual(cus_1.phone_number, '212-576-4000')
        self.assertEqual(cus_1.status, True)

        cus_2 = cm.Customer.get(cm.Customer.customer_id == 200)
        self.assertEqual(cus_2.customer_id, 200)
        self.assertEqual(cus_2.home_address,
                         '17801 International Blvd, Seattle, WA 98101')
        self.assertEqual(cus_2.email_address, 'iron.man@gmail.com')

        cus_3 = cm.Customer.get(cm.Customer.customer_id == 300)
        self.assertEqual(cus_3.customer_id, 300)
        self.assertEqual(cus_3.status, False)
        self.assertEqual(cus_3.credit_limit, 7078)

    def test_search_customer(self):
        """Test searching for a customer"""
        bo.add_customer(100, 'Peter', 'Parker',
                        '135 W. 50th Street, New York City, NY 10011',
                        '212-576-4000', 'peter.parker@marvel.com',
                        True, 1000)

        actual = bo.search_customer(100)
        expected = {'first_name': 'Peter', 'last_name': 'Parker',
                    'email_address': 'peter.parker@marvel.com',
                    'phone_number': '212-576-4000'}
        self.assertEqual(actual, expected)

    def test_search_customer_fail(self):
        """Test searching for a customer (fail)"""
        actual = bo.search_customer(100)  # Not in table
        expected = dict()
        self.assertEqual(actual, expected)

    def test_delete_customer(self):
        """Test deleting a customer"""
        bo.add_customer(100, 'Peter', 'Parker',
                        '135 W. 50th Street, New York City, NY 10011',
                        '212-576-4000', 'peter.parker@marvel.com',
                        True, 1000)

        bo.delete_customer(100)
        actual = bo.search_customer(100)
        expected = dict()
        self.assertEqual(actual, expected)

    def test_delete_customer_fail(self):
        """Test deleting a customer (fail)"""
        with self.assertRaises(ValueError):
            bo.delete_customer(100)  # Not in table

    def test_update_customer_credit(self):
        """Test updating customer credit limit"""
        bo.add_customer(100, 'Peter', 'Parker',
                        '135 W. 50th Street, New York City, NY 10011',
                        '212-576-4000', 'peter.parker@marvel.com',
                        True, 1000)

        bo.update_customer_credit(100, 2000)
        cus = cm.Customer.get(cm.Customer.customer_id == 100)
        actual = cus.credit_limit
        expected = 2000
        self.assertEqual(actual, expected)

    def test_update_customer_credit_fail(self):
        """Test updating customer credit limit (fail)"""
        with self.assertRaises(ValueError):
            bo.update_customer_credit(100, 2000)  # Not in table

    def test_list_active_customers(self):
        """Test listing active customers"""
        bo.add_customer(100, 'Peter', 'Parker',
                        '135 W. 50th Street, New York City, NY 10011',
                        '212-576-4000', 'peter.parker@marvel.com',
                        True, 1000)
        bo.add_customer(200, 'Iron', 'Man',
                        '17801 International Blvd, Seattle, WA 98101',
                        '206-787-5388', 'iron.man@gmail.com',
                        True, 5000)
        bo.add_customer(300, 'Ramkumar', 'Rajanbabu',
                        '7525 166th Ave NE, Redmond, WA 98052',
                        '425-556-2900', 'ram.kumar@gmail.com',
                        False, 7078)

        self.assertEqual(bo.list_active_customers(), 2)

    def test_display_customers(self):
        """Testing display customers"""
        bo.add_customer(100, 'Peter', 'Parker',
                        '135 W. 50th Street, New York City, NY 10011',
                        '212-576-4000', 'peter.parker@marvel.com',
                        True, 1000)
        bo.add_customer(200, 'Iron', 'Man',
                        '17801 International Blvd, Seattle, WA 98101',
                        '206-787-5388', 'iron.man@gmail.com',
                        True, 5000)

        cus = bo.display_customers()
        expected = "Iron Man"
        self.assertEqual(cus[1], expected)


if __name__ == "__main__":
    unittest.main()
