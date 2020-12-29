from mongoengine import Document, fields


class Carrier(Document):
    name = fields.StringField(max_length=100)
    address = fields.StringField()
    phone = fields.StringField(max_length=15)

    meta = {'collection': 'carriers'}


class Vehicle(Document):
    plate = fields.StringField(max_length=20)
    model = fields.StringField(max_length=100)
    vin = fields.StringField(max_length=100)
    vrc = fields.StringField(max_length=100)
    year = fields.StringField(max_length=4)
    owner = fields.StringField(max_length=100)
    carrier = fields.ReferenceField(Carrier)
    route = fields.StringField(max_length=100)
    internalId = fields.StringField(max_length=20)
    kilometres = fields.FloatField()
    repairs = fields.FloatField()

    meta = {'collection': 'vehicles'}


class Tag(Document):
    name = fields.StringField(max_length=100)

    meta = {'collection': 'tags'}


class Issue(Document):
    name = fields.StringField(max_length=20)
    tags = fields.ListField(fields.ReferenceField(Tag))
    description = fields.StringField()
    createdAt = fields.DateTimeField()
    resolved = fields.DateTimeField()
    vehicle = fields.ReferenceField(Vehicle)

    meta = {'collection': 'issues'}


class Route(Document):
    name = fields.StringField(max_length=100)
    number = fields.StringField(max_length=15)
    startTime = fields.StringField(max_length=10)
    endTime = fields.StringField(max_length=10)
    carrier = fields.ReferenceField(Carrier)

    meta = {'collection': 'routes'}


class Survey(Document):
    vehicle = fields.ReferenceField(Vehicle)
    date = fields.StringField()
    route = fields.StringField(max_length=10)
    startTime = fields.StringField(max_length=10)
    endTime = fields.StringField(max_length=10)
    distance = fields.IntField()
    cashPassengers = fields.IntField()
    blackCounter = fields.IntField()
    redCounter = fields.IntField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        self.users = []
        self.issues = []
    meta = {'collection': 'surveys'}


class User(Document):
    login = fields.StringField(max_length=100)
    code = fields.StringField(max_length=100)
    name = fields.StringField(max_length=100)
    carrier = fields.StringField()
    role = fields.StringField(max_length=50)
    internalId = fields.StringField(max_length=50)
    licence = fields.StringField(max_length=100)

    meta = {'collection': 'users'}

    def get_id_as_str(self):
        return self.id


class VehiclePin(Document):
    user = fields.StringField()
    vehicle = fields.StringField()

    meta = {'collection': 'vehiclepins'}
