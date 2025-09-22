# test/test_user_management.py
import pytest
import pyotp
from src.user_management import create_user
from src.user_management import verify_totp

def test_verify_totp_correct_code():
    """
    Tests that a correct TOTP code is successfully verified.
    """
    # This secret is for demonstration; in a real app, it would be retrieved
    # for a specific user.
    totp_secret = "JBSWY3DPEHPK3PXP" # A known secret for a predictable code
    totp = pyotp.TOTP(totp_secret)
    correct_code = totp.now() 
    
    assert verify_totp(correct_code, totp_secret) is True
    
def test_verify_totp_incorrect_code():
    """
    Tests that an incorrect TOTP code fails verification.
    """
    totp_secret = "JBSWY3DPEHPK3PXP"
    incorrect_code = "123456"
    
    assert verify_totp(incorrect_code, totp_secret) is False
    
def test_create_user_generates_totp_secret():
    """
    Test that a new user is created with a username, 
    a TOTP secret, and a QR code URI.
    """
    username = "test_user@example.com"
    user_data = create_user(username)
    
    assert user_data["username"] == username
    assert "totp_secret" in user_data
    assert "qr_code_uri" in user_data
    assert user_data["totp_secret"] is not None
    assert user_data["qr_code_uri"] is not None