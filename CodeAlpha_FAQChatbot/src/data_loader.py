def load_faqs(file_path):
    faq_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            question, answer = line.strip().split("|")
            faq_data.append((question, answer))

    return faq_data
