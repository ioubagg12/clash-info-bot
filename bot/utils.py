def format_tag(tag):
    if not tag.startswith('#'):
        return f"#{tag}"
    return tag
