from voluptuous import Schema, Required, All, Length

schema_login = Schema({
    Required('email'): All(str, Length(min=1)),
    Required('password'): All(str, Length(min=1))
})
