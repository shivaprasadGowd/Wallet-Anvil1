from ._anvil_designer import paycontactsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class paycontacts(paycontactsTemplate):
    def __init__(self, user=None, **properties):
        try:
            self.user = user
            
            # Set Form properties and Data Bindings.
            self.init_components(**properties)
            print("User:", self.user)
            
            phonenumber = app_tables.wallet_users.search()
            
            # Set the fetched data as the items for the repeating panel
            self.repeating_panel_1.items = phonenumber
            # Pass the user information to each ItemTemplate9 instance
            for item in self.repeating_panel_1.items:
                self.repeating_panel_1.add_component(ItemTemplate9(user=self.user, item=item))
        
        except Exception as e:
            print("Error in __init__:", e)
            # Handle the error here

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            open_form('customer.interaction', user=self.user)
        except Exception as e:
            print("Error in button_1_click:", e)
            # Handle the error here

    def text_box_1_pressed_enter(self, **event_args):
        entered_user = self.text_box_1.text

        # Convert entered_user to a number if it's a valid numerical value
        try:
            entered_user = int(entered_user)  # Assuming phone numbers are integers
        except ValueError:
            # Handle the case where entered_user is not a valid numerical value
            # You might want to display an error message or handle this case differently
            print("Entered user is not a valid numerical value.")
            return

        # Filter transactions based on the entered user
        filtered_transactions = app_tables.wallet_users.search(phone==entered_user)

        # Update the repeating panel with the filtered transactions
        self.repeating_panel_1.items = filtered_transactions
