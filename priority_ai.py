# функція для визначення пріоритету задачі на основі тексту
def assign_priority(text):
    text = text.lower()
    if any(word in text for word in ["терміново", "зараз", "негайно"]):
        return "Високий"
    elif any(word in text for word in ["сьогодні", "важливо", "до кінця дня"]):
        return "Середній"
    else:
        return "Низький"
