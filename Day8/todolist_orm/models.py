import datetime

import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase


db = PostgresqlExtDatabase('todo_list')


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now())
    updated_at = pw.DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
        # Check this one out here http://docs.peewee-orm.com/en/latest/peewee/models.html#table-names
        legacy_table_names = False

# Define your models here


# # table of users
class UserName(BaseModel):
    owner_name = pw.CharField()
    password = pw.CharField(default='111111')


# table : different kind of list
class TodoList(BaseModel):
    name = pw.CharField()
    list_owner = pw.ForeignKeyField(UserName, backref='owner')


# each tasks
class TodoTask(BaseModel):
    task = pw.CharField()
    completed = pw.CharField(default='not done')
    todo_list = pw.ForeignKeyField(TodoList, backref='todos')


print(" ")
print("model.py uploaded")
print(" ")
