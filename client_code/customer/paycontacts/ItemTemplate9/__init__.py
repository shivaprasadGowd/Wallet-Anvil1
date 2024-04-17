from ._anvil_designer import ItemTemplate9Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate9(ItemTemplate9Template):
    def __init__(self, user=None, **properties):
        self.user = user
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        # Access the data for the selected user
        selected_user = self.item  # Assuming you have set the 'item' property of the repeating panel to the user row
        
        # Extract the phone number from the selected user
        phone_number = selected_user['phone']  # Assuming 'phone' is the key for the phone number in your data
        
        # Open the customer.interaction form and pass the phone number and user information
        open_form('customer.interaction', phone_number=phone_number, user=self.user)


  

  
