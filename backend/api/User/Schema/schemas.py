from voluptuous import Schema, Required, All, Length

schema_insert_user = Schema({
    Required('nomeRegistro'): All(str, Length(min=1)),
    Required('niverRegistro'): All(str, Length(min=1)),
    Required('emailRegistro'): All(str, Length(min=1)),
    Required('celRegistro'): All(str, Length(min=1)),
    Required('senhaRegistro'): All(str, Length(min=1))
})
