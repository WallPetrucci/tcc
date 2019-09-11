from voluptuous import Schema, Required, All, Length

schema_insert_address = Schema({
    Required('street'): All(str, Length(min=1)),
    Required('number'): All(str, Length(min=1)),
    Required('city'): All(str, Length(min=1)),
    Required('country'): All(str, Length(min=1)),
    Required('state'): All(str, Length(min=1)),
    Required('neighborhood'): All(str, Length(min=1)),
    Required('User_idUser'): int,
})

schema_update_address = Schema({
    'street': All(str, Length(min=1)),
    'number': All(str, Length(min=1)),
    'city': All(str, Length(min=1)),
    'country': All(str, Length(min=1)),
    'state': All(str, Length(min=1)),
    'neighborhood': All(str, Length(min=1)),
    'User_idUser': int,
})