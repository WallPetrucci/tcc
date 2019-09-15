from voluptuous import Schema, Required, All, Length

schema_insert_settings = Schema({
    Required('heartRate'): {
        Required("max"): All(str, Length(min=1)),
        Required("min"): All(str, Length(min=1))
    },
    Required('oximetry'): {
        Required("max"): All(str, Length(min=1)),
        Required("min"): All(str, Length(min=1))
    },
    Required('temperature'): {
        Required("max"): All(str, Length(min=1)),
        Required("min"): All(str, Length(min=1))
    },
    Required('activeAlertOximetry'): int,
    Required('activeAlertHeartRate'): int,
    Required('activeAlertTemperature'): int,
    Required('User_idUser'): int,
})


schema_update_settings = Schema({
    'heartRate': {
        "max": All(str, Length(min=1)),
        "min": All(str, Length(min=1))
    },
    'oximetry': {
        "max": All(str, Length(min=1)),
        "min": All(str, Length(min=1))
    },
    'temperature': {
        "max": All(str, Length(min=1)),
        "min": All(str, Length(min=1))
    },
    'activeAlertOximetry': int,
    'activeAlertHeartRate': int,
    'activeAlertTemperature': int
})