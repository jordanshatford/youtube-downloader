# Validate that a user has actually entered a value
def validate_value_entered(value: str) -> str | bool:
    return True if len(value) > 0 else 'Please enter a value.'
