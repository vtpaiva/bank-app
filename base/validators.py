from django.core.exceptions import ValidationError

def cpf_validator(cpf: str):
    if not cpf.isdigit() or len(cpf) != 11:
        raise ValidationError(f"The cpf field needs to have 11 numeric digits. Received: (Is digit? {cpf.isdigit()}, Lenght: {len(cpf)})")
    
