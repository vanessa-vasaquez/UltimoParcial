from Order import Order

class OrderDetails:
  OrderId:str
  ProductId:str
  ProductName:str
  Quatity:int
  UnitCost:float
  Total:float
  order: Order

  def __init__(self, order):
        self.order = Order 

  def calculatetotal(self):
    print