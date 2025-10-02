import pyotp

def create_user(username: str) -> dict:
    """
    Generates a new user profile with a TOTP secret and provisioning URI.
    
    Args:
        username: The user's identifier, typically an email address.
        
    Returns:
        A dictionary containing the username, the generated TOTP secret, 
        and the provisioning URI for QR code generation.
    """
    
    totp_secret = pyotp.random_base32()
    qr_code_uri = pyotp.totp.TOTP(totp_secret).provisioning_uri(
        name=username,
        issuer_name="DigitalDeadMansSwitch"
    )
    
    return {
        "username": username,
        "totp_secret": totp_secret,
        "qr_code_uri": qr_code_uri
    }