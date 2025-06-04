📚 CS50 Web – Week 3: SQL, Models & Migrations

────────────────────────────────────────────
🗃️ SQL Basics
────────────────────────────────────────────
- SQL = Structured Query Language (used to manage relational databases).
- SQLite Types:
  - Text
  - Numeric
  - Integer
  - Real
  - Blob(Binary large object)

- MySQL Types
  - Char(size)
  - Varchar(size)
  - Smallint
  - int
  - Bigint
  - Float
  - Double

- Core Commands:
  - CREATE TABLE, INSERT INTO, SELECT, UPDATE, DELETE, ALTER, JOIN, CREATE INDEX
  - WHERE, AND, OR, ON, LIKE, IN, LIMIT, GROUP BY, ORDER BY, HAVINGV  (filters), COUNT, AVERAGE, MIN, MAX, SUM, SET

     CREATE INDEX name_index ON passengers(last);
     
- SQL Injection
- Race Condition(multiple things happenening on the same thing ) 

- Data Types: INTEGER, TEXT, REAL, BOOLEAN, DATE
- Constraints:
  - PRIMARY KEY: Unique row ID
  - NOT NULL: Required field
  - UNIQUE: No duplicates
  - FOREIGN KEY: References another table
  - DEFAULT: IF there is no value for that particular field then default value is given
  - CHECK: To check if the values are within a particular range  

────────────────────────────────────────────
🔌 Django Models
────────────────────────────────────────────
- Define models as Python classes in models.py
Example:
from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"

- Common Field Types:
  CharField, IntegerField, BooleanField, DateTimeField, ForeignKey, ManyToManyField

────────────────────────────────────────────
🔁 Migrations
────────────────────────────────────────────
- makemigrations → create migration files from model changes
- migrate → apply migrations to DB
- sqlmigrate app 0001 → show SQL from a migration
- showmigrations → see all migrations and their status

────────────────────────────────────────────
🔗 Relationships
────────────────────────────────────────────
- One-to-Many (ForeignKey):
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

- Many-to-Many:
class Passenger(models.Model):
    name = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

────────────────────────────────────────────
🛠️ Django Shell
────────────────────────────────────────────
- Launch with: python manage.py shell
- Example:
from flights.models import Flight
f = Flight(origin="New York", destination="London", duration=415)
f.save()
- To query the database like get all the objects.
Flight.objects.all()

Airport.objects.filter(city="New York")

- Operations: .all(), .filter(), .get(), .create(), .update(), .delete(), .first()

────────────────────────────────────────────
🖥️ Django Admin
────────────────────────────────────────────
- Enable admin interface:
  - python manage.py createsuperuser
  - Register models in admin.py:
    from .models import Flight
    class FlightAdmin(admin.ModelAdmin):
       list_display = ("id","orgin")
       filter_horizontal = ("flights",)
    admin.site.register(Flight,FlightAdmin)



from django.contrib.auth import authenticate, login, logout

user = authenticate(request,username=username,password=password)
if user is not None:
   login(reques,user)
   return HttpResponseRedirect(reverse("index"))
else:
   return render(request."users/login.html",{"message": "Invalid credentials."})

{% url 'flight' flight.id %}

request.user.is_authenticated:

────────────────────────────────────────────
✅ Summary
────────────────────────────────────────────
✔ SQL helps manage relational data
✔ Models = DB schema in Python
✔ Migrations = sync code with DB
✔ Use related_name for reverse relations
✔ Use Django shell and admin for testing
