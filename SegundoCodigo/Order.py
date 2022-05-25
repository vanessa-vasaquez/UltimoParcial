from datetime import date

from SegundoCodigo.Customer import Costumer


class Order:
  Orderid:str
  Date:date
  CostumerName:Costumer
  CostumerId:str

  def _init_(self,costumer:Costumer):
    self.usuario=costumer

  def placeorder(self):
    print("se asignara un lugar a la orden")