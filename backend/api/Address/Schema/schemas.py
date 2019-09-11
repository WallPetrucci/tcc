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