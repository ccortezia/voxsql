
SOURCE = """/**Simple sentence
 *@dialect postgresql
 *@name count_all
 *@retmode scalar
 ************** */
{select count(*) from contacts;
}
"""

HEADER = """Simple sentence
@dialect postgresql
@name count_all
@retmode scalar
"""

HEADER_DESC = """Simple sentence
"""

BODY = """select count(*) from contacts;
"""

FRAMES = [
    {
        'base': {
            'source': SOURCE,
            'header': HEADER,
            'body': BODY,
        },
        'header': {
            'source': HEADER,
            'name': 'count_all',
            'desc': HEADER_DESC,
            'dialect': 'postgresql',
            'params': [],
            'retmode': 'scalar',
            'retvals': [],
        },
        'body': {
            'source': BODY
        }
    }
]
