
class Account:

    """
    class that generates new instances of account_list = [] # Empty accounts list
    users accounts.
    """

    # account_list = [] # Empty account list

    def __init__(self, account_name, account_password):

        self.account_name = account_name
        self.account_password = account_password

    account_list = []

    def save_accounts(self):
        """
        metod that saves accounts object into the list
        """
        self.account_list.append(self)

    def delete_accounts(self):
        """
        metod that deletes accounts
        """
        Account.account_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        """
        a method that takes in a name and returnsan account that matches that name

        Args:
         name:account_name that has a password
        return:
        the account that matches that name
        """

        for accounts in cls.account_list:
            if accounts.account_name == account_name:
                return accounts

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def account_exist(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.account_list:
            if account.phone_number == number:
                return True

        return False
