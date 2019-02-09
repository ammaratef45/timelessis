"""File for models in items module"""
from datetime import datetime
from timeless import DB

class Item(DB.Model):
    """Model for item entity
    @todo #15:30min Continue the implementation. Items must have their own
     management pages to list, create, edit, and delete them. On the index
     page, you should be able to sort and filter for each column.
    """
    __tablename__ = "items"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, nullable=False)
    stock_date = DB.Column(DB.DateTime, nullable=False)
    comment = DB.Column(DB.String, nullable=True)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)
    employee_id = DB.column(DB.Integer, DB.ForeignKey("employees.id"))
    company = DB.relationship("Company", back_populates="items")
    employee = DB.relationship("employee", back_populates="items")

    def assign(self, employee):
        """Assign the item to an employee"""
        self.employee_id = employee.id


    def __repr__(self):
        """Return object information - String"""
        return "<Item %r>" % self.name

class ItemHistory(DB.Model):
    """ Model for history of item assigning
    @todo #142:30min Continue implementatin.
     create a record here every time assign function is called.
     update a record if assign is called and employee_id in item is not null.
    """
    __tablename__ = "itemHistory"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    employee_id = DB.column(DB.Integer, DB.ForeignKey("employees.id"))
    item_id = DB.column(DB.Integer, DB.ForeignKey("items.id"))
    start_time = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    end_time = DB.Column(DB.DateTime)
    employee = DB.relationship("employee", back_populates="itemHistory")
    item = DB.relationship("items", back_populates="itemHistory")

    def __repr__(self):
        """Return object information - String"""
        return "<Item %r>" % self.name