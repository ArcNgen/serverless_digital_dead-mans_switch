# test/test_user_management.py
import pytest
from src.user_management import create_user

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