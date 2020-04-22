class User:
    """
    Class that generates new instances of a user login.
    """

    user_list = []  

    def __init__(self,user_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.password = password
    
    def save_user(self):
      '''
      save_user method saves a new user object to the user_list
      '''
      User.user_list.append(self)