from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.card_1.visible = False
    self.card_3.visible = False
    self.card_5.visible = False

  def link_8_click(self, **event_args):
    self.card_1.visible = not self.card_1.visible
    self.card_3.visible = False
    self.card_5.visible = False

  def link_13_click(self, **event_args):
    self.card_3.visible = not self.card_3.visible
    self.card_1.visible = False
    self.card_5.visible = False

  def link_15_click(self, **event_args):
    self.card_5.visible = not self.card_5.visible
    self.card_1.visible = False
    self.card_3.visible = False

  def link_16_click(self, **event_args):
    pass

  def button_3_click(self, **event_args):
    open_form('Login')

  def button_1_click(self, **event_args):
    open_form('Login')

  