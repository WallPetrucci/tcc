from voluptuous import Schema, Required, All, Length

schema_insert_monitor = Schema({
    Required('name'): All(str, Length(min=1)),
    Required('email'): All(str, Length(min=1)),
    Required('telephone'): All(str, Length(min=1)),
    Required('id_user'): int
})

schema_update_monitor = Schema({
    'name': All(str, Length(min=1)),
    'email': All(str, Length(min=1)),
    'telephone': All(str, Length(min=1)),
    'idMonitor': int
})

schema_monitoring = Schema({
    'token': All(str, Length(min=15, max=16)),
})
