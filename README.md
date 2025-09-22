# AWS Digital Dead Man's Switch

This project is a serverless application that acts as a digital dead man's switch. If the user fails to perform a periodic check-in, the system will automatically notify a list of pre-defined recipients.

## How It Works

The system is built on a serverless AWS architecture. The core logic is as follows:

1.  **User Setup**: A user configures their switch, defining the check-in frequency (e.g., every 30 days) and the contact details for their recipients. A Time-based One-Time Password (TOTP) secret is generated for the user to save in an authenticator app (like Google Authenticator).
2.  **Scheduled Check**: An Amazon EventBridge rule runs on a schedule (e.g., daily) to check for users who have missed their check-in deadline.
3.  **Check-In**: To prevent alerts from being sent, the user must periodically "check in" by providing a valid TOTP code from their authenticator app. This action resets their check-in timer.
4.  **Alerts**: If the scheduled check finds that a user's check-in deadline has passed, it triggers an alert mechanism, which uses Twilio to send SMS messages to all of the user's designated recipients.

## Technology Stack

*   **Backend**: Python
*   **AWS Services**:
    *   AWS Lambda: For running the serverless functions (user setup, check-in, alert logic).
    *   Amazon DynamoDB: A NoSQL database to store user data, recipient lists, and check-in timestamps.
    *   Amazon EventBridge: To schedule the periodic checks for missed check-ins.
    *   AWS SAM (Serverless Application Model): For defining the infrastructure as code.
*   **Notifications**: Twilio API (for SMS)
*   **Authentication**: TOTP (e.g., Google Authenticator)
*   **Development**: Test-Driven Development (TDD) using `pytest`.

## Project Structure

```
.
├── README.md
├── src/
│   ├── __init__.py
│   └── user_management.py
└── tests/
    ├── __init__.py
    └── test_user_management.py
```

## Core Components

### User Management (`src.user_management`)

*   `create_user(username: str) -> dict`:
    *   **Purpose**: Generates a new user profile.
    *   **Arguments**:
        *   `username` (str): The user's identifier, typically an email.
    *   **Returns**: A dictionary containing the `username`, a new `totp_secret` (for storing), and a `qr_code_uri` (for displaying to the user).

## Development

This project follows a Test-Driven Development (TDD) approach. All new functionality should begin with a failing test that is then made to pass.

To set up the local environment:

1.  Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run tests:
    ```bash
    pytest
    ```