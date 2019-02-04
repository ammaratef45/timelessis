"""File for models in test_companies module"""
from timeless.models import TimestampsMixin

from timeless.db import DB


class Company(TimestampsMixin, DB.Model):
    """Model for company business entity.
    @todo #3:30min Create management pages for Companies to list, create, edit
     and delete them. In the index page it should be possible to sort and filter
     for every column.
    @todo #3:30min Implement TimestampMixin, like in the example
     (http://flask-sqlalchemy.pocoo.org/2.3/customizing/). Change all the models
     to use this mixin instead of existing created_on and updated_on fields.
    """
    __tablename__ = "companies"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, unique=True, nullable=False)
    code = DB.Column(DB.String, unique=True, nullable=False)
    address = DB.Column(DB.String)

    locations = DB.relationship("Location", order_by="Location.id",
                                back_populates="company")
    employees = DB.relationship("Employee", order_by="Employee.id",
                                back_populates="company")
    roles = DB.relationship("Role", order_by="Role.id",
                            back_populates="company")

    def __repr__(self):
        return "<Company %r>" % self.name
