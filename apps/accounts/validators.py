from django.core.validators import RegexValidator

phone_regex_validator = RegexValidator(
    regex=r"^989\d{2}\d{3}\d{4}$", message="Invalid phone number.")
