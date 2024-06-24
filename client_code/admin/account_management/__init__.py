from ._anvil_designer import account_managementTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .ItemTemplate6 import ItemTemplate6

class account_management(account_managementTemplate):
    def __init__(self, user=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user = user
        if user is not None:
            self.label_656.text = user['users_username']
        
        self.refresh_users()  # Load all users initially
        ItemTemplate6.user = self.user

    def refresh_users(self, username_filter=None, status_filter=None, filter_customers=False):
        # Fetch all users from the table
        users = app_tables.wallet_users.search()
        
        # Filter users based on customer type if filter_customers is True
        if filter_customers:
            users = [user for user in users if user['users_usertype'] == 'customer']

        # Filter users based on status if status filter is provided
        if status_filter == "Active":
            users = [user for user in users if user['users_inactive'] is None and user['users_hold'] is None]
        elif status_filter == "Inactive":
            users = [user for user in users if user['users_inactive'] is True]
        elif status_filter == "Hold":
            users = [user for user in users if user['users_hold'] is True]

        # Filter users based on username if username filter is provided
        if username_filter:
            users = [user for user in users if user['users_username'].lower().startswith(username_filter.lower())]

        # Create a list of dictionaries with status color for display purposes
        user_list = []
        for user in users:
            user_dict = dict(user)
            if user['users_hold']:
                user_dict['status_color'] = 'red'
            elif user['users_inactive']:
                user_dict['status_color'] = 'gray'
            else:
                user_dict['status_color'] = 'green'
            user_list.append(user_dict)

        # Set items in the repeating panel
        self.repeating_panel_1.items = user_list
        self.label_5.text = f"Total users: {len(user_list)}"

    def button_2_click(self, **event_args):
        # Handle search button click event to refresh users based on entered username
        username_filter = self.text_box_1.text
        self.refresh_users(username_filter)

    def link_8_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.refresh_users(filter_customers=True)  # Filter for customers only
        open_form('admin', user=self.user)

    def link_10_copy_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.user_support', user=self.user)

    

    def button_3_click(self, **event_args):
        open_form('admin.admin_add_user', user=self.user)

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin', user=self.user)

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.report_analysis', user=self.user)

    def link_7_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.transaction_monitoring', user=self.user)

    def link_6_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass

    def link_5_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('admin.add_currency', user=self.user)

    def link_4_click(self, **event_args):
        open_form('admin.admin_add_user', user=self.user)

    def link_3_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass

    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        # Get the selected status filter
        status_filter = self.drop_down_1.selected_value

        # Refresh users based on the selected status filter
        self.refresh_users(status_filter=status_filter)

   d

    def link_9_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass

    def link_10_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass
