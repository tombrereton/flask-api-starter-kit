def parse_as_bool(text: str):
    return text is not None and text.lower() == 'true'
