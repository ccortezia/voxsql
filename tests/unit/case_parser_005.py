
SOURCE = """/**
 *
 * Do something
 *
 * @dialect postgresql
 * @name get_contacts
 * @param contact_name: string - the name
 * @param contact_origin: string - the origin
 * @retmode tuples
 */
{
    select * from contacts
    where name=%(contact_name)s and origin=%(contact_origin)s
    ;
}
"""

HEADER = """Do something

@dialect postgresql
@name get_contacts
@param contact_name: string - the name
@param contact_origin: string - the origin
@retmode tuples
"""

HEADER_DESC = """Do something
"""

BODY = """select * from contacts
where name=%(contact_name)s and origin=%(contact_origin)s
;
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
            'name': 'get_contacts',
            'desc': HEADER_DESC,
            'dialect': 'postgresql',
            'params': [
                {
                    'source':  '@param contact_name: string - the name\n',
                    'name': 'contact_name',
                    'type': 'string',
                    'desc': 'the name\n'
                },
                {
                    'source':  '@param contact_origin: string - the origin\n',
                    'name': 'contact_origin',
                    'type': 'string',
                    'desc': 'the origin\n'
                }
            ],
            'retmode': 'tuples',
            'retvals': [],
        },
        'body': {
            'source': BODY
        }
    }
]
