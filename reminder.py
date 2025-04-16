from plyer import notification


# Функція для відправки сповіщення коли створюється нова задача
def send_reminder(text):
    notification.notify(title="Нова задача", message=text, timeout=5)
