import random


def check_system_status():
    return {
        "wifi_server": "Online",
        "portal_server": "Online",
        "email_server": "Online",
        "printer_server": "Online"
    }


def log_ticket(problem):
    ticket_number = random.randint(1000, 9999)

    return {
        "success": True,
        "ticket_id": ticket_number,
        "problem": problem,
        "message": f"Support ticket #{ticket_number} created successfully."
    }