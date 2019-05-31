import textwrap


def text_block(text):
    dedented_text = textwrap.dedent(text)
    stripped_text = dedented_text.strip() + '\n'
    return stripped_text if stripped_text.strip() else stripped_text.strip()


def text_field(text):
    dedented_text = textwrap.dedent(text)
    stripped_text = dedented_text.strip()
    return stripped_text
