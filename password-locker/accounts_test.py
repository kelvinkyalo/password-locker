import unittest  # Importing the unittest module
from accounts import Account  # Importing the user class


class TestAccounts(unittest.TestCase):

    '''
    Test class that defines test cases for the accounts class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_accounts = Account("facebook", "1234")
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.accounts_list = []

    def test_accounts_instance(self):
        """
        method to test if the new accounts have been instanciated properly
        """        
        self.assertEqual(self.new_accounts.account_name, "facebook")
        self.assertEqual(self.new_accounts.account_password, "1234")

    def test_save_accounts(self):
        """
        testcase to test if account objects have been saved
        """
        self.new_accounts.save_accounts()  # saving the new account
        self.assertEqual(len(Account.accounts_list), 1)
   
    def test_delete_accounts(self):
        """
        testcase to delete account
        """
        self.new_accounts.save_accounts()
        test_accounts = Account("facebook","1234")
        test_accounts.save_accounts()
        self.new_accounts.delete_accounts() #to delete an account object
        self.assertEqual(len(Account.account_list),1)

    def test_find_accounts_by_name(self):
        """
        test to check if accounts by the  account name and can display information
        """
        self.new_accounts.save_accounts()
        test_accounts = Account("facebook","1234")
        test_accounts.save_accounts()

    def test_display_all_accounts(self):
        """
        test to check if all contacts can be veiwed
        """
        self.assertEqual(Account.display_accounts(),Account.account_list)

    
if __name__ == '__main__':
    unittest.main()
