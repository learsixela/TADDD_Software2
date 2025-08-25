# examples/modular_bad/emailer.py
def send_email(to: str, message: str):
    print(f"[EMAIL] To: {to} | Body: {message}")
