from voxsql.parser import parse


# TODO: remove this utility once loading becomes a primary library functionality
def load_functions(text, binder_cls):

    frames = parse(text)

    function_sources = [binder_cls().create(frame) for frame in frames]

    for source_code in function_sources:
        print(source_code)
        exec(source_code)

    retdict = {}
    for frame in frames:
        # NOTE: dict comprehensions do not work here.
        retdict[frame.header.name] = locals()[frame.header.name]

    return retdict
