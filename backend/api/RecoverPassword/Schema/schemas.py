from voluptuous import Schema, Required, All, Length

schema_recovery = Schema({
    Required('email'): All(str, Length(min=1)),
})
