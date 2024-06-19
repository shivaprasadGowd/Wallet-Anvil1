from ._anvil_designer import adminTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import datetime
from anvil.tables import app_tables
class admin(adminTemplate):
    def __init__(self, user=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user = user
        #self.total_user.text = anvil.server.call('total_users',self.user['users_usertype'])
        if user is not None:
            self.label_4.text = user['users_username']
            #self.image_3.source=user['users_profile_pic']
        self.refresh_data()
        self.check_profile_pic()

  
    def check_profile_pic(self):
      user_data = app_tables.wallet_users.get(users_email=str(self.user['users_email'])) #changed
      if user_data:
        existing_img = user_data['users_profile_pic']
        if existing_img != None:
          self.image_3.source = existing_img
        else: 
          print('no pic')
      else:
        print('none')

  
    def refresh_data(self):
    # Call the server function to get transactions data
      transactions = anvil.server.call('get_transactions')
    
      # Check if there are no transactions
      if not transactions:
          self.plot_1.data = [go.Scatter(x=[0], y=[0], mode='text', text=['No transactions'], textposition='middle center')]
          self.plot_1.layout = go.Layout(
              title='Monthly Credit Transactions in Wallet by Currency',
              xaxis=dict(title='Month'),
              yaxis=dict(title='Amount')
          )
          self.plot_1.visible = True
          return
  
      # Filter transactions to include only 'Credit' type
      credit_transactions = [t for t in transactions if t['users_transaction_type'] == 'Credit']
  
      # Identify all years present in the transactions
      years = sorted(set(transaction['users_transaction_date'].year for transaction in credit_transactions))
  
      # Identify all currency types present in the transactions
      currency_types = sorted(set(transaction['users_transaction_currency'] for transaction in credit_transactions))
  
      # Organize data for plotting (aggregate by month and sum credit amounts for each currency)
      credit_by_month_and_currency = {currency: {} for currency in currency_types}
      for currency in currency_types:
          for year in years:
              for month in range(1, 13):
                  key = f"{year}-{month:02}"
                  credit_by_month_and_currency[currency][key] = 0
  
      for transaction in credit_transactions:
          date = transaction['users_transaction_date'].strftime("%Y-%m")  # Format date as string for grouping
          currency = transaction['users_transaction_currency']
          credit_by_month_and_currency[currency][date] += transaction['users_transaction_fund']
  
      # Define colors for different currency types
      colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgoldenrodyellow', 'lightgray', 'lightcyan']
      currency_color_map = {currency: colors[i % len(colors)] for i, currency in enumerate(currency_types)}
  
      # Create data for plotting
      all_months = sorted(set(key for currency in currency_types for key in credit_by_month_and_currency[currency].keys()))
      plot_data = []
  
      for currency in currency_types:
          credit_values = [credit_by_month_and_currency[currency].get(month, 0) for month in all_months]
          plot_data.append(go.Bar(
              x=all_months, 
              y=credit_values, 
              name=f'Credit ({currency})', 
              marker_color=currency_color_map[currency]
          ))
  
      # Set the initial visible range to the last 12 months if available
      if len(all_months) >= 12:
          initial_visible_range = [all_months[-12], all_months[-1]]
      elif len(all_months) > 0:
          initial_visible_range = [all_months[0], all_months[-1]]
      else:
          initial_visible_range = []
  
      # Plot the data
      self.plot_1.data = plot_data
  
      # Set the layout to include month and year labels, highlighting current year
      self.plot_1.layout = go.Layout(
          title='Monthly Credit Transactions in Wallet by Currency',
          xaxis=dict(
              title='Month',
              tickmode='array',
              tickvals=all_months,
              ticktext=[datetime.datetime.strptime(month, "%Y-%m").strftime("%Y-%b") for month in all_months] if all_months else [],
              range=initial_visible_range  # Set the initial visible range
          ),
          yaxis=dict(title='Amount'),
          barmode='group'
      )
  
      self.plot_1.visible = True




    def link_1_click(self, **event_args):
        open_form('admin.report_analysis',user=self.user)

    def link_2_click(self, **event_args):
        open_form('admin.account_management',user = self.user)

    def link_3_click(self, **event_args):
        open_form('admin.transaction_monitoring',user=self.user)

    def link_4_click(self, **event_args):
        open_form('admin.admin_add_user',user=self.user)

    def link_5_click(self, **event_args):
        open_form('admin.audit_tra',user=self.user)

    def link_6_click(self, **event_args):
        open_form('admin.raise_a_complaint',user=self.user)

    def link_7_click(self, **event_args):
        open_form('admin.show_users',user=self.user)

    def link_9_click(self, **event_args):
        open_form('admin.create_admin',user=self.user)

    def link_10_click(self, **event_args):
        open_form('admin.add_currency',user=self.user)

    def plot_1_click(self, points, **event_args):
      """This method is called when a data point is clicked."""
      pass

    
