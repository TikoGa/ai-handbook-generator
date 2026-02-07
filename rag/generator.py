def generate_answer(context: str, question: str) -> str:
    return (
        "Based on the uploaded document, the following relevant information was found:\n\n"
        + context[:1800]
    )
