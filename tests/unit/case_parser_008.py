
SOURCE = """/**
 *
 * Do something amazing
 *
 * @dialect postgresql
 * @name add_contact
 * @param contact_name: string - the name
 *   drives the process.
 * @retmode record
 * @retval contact_id: number - an identifier
 *   to be returned.
 * @retval contact_name: string - the name,
 * to be returned.
 */
{
    insert into contacts (name)
    values (%(contact_name)s)
    returning id, name
    ;
}
"""

HEADER = """Do something amazing

@dialect postgresql
@name add_contact
@param contact_name: string - the name
  drives the process.
@retmode record
@retval contact_id: number - an identifier
  to be returned.
@retval contact_name: string - the name,
to be returned.
"""

HEADER_DESC = """Do something amazing
"""

BODY = """insert into contacts (name)
values (%(contact_name)s)
returning id, name
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
            'name': 'add_contact',
            'desc': HEADER_DESC,
            'dialect': 'postgresql',
            'params': [
                {
                    'source': '@param contact_name: string - the name\n  drives the process.\n',
                    'name': 'contact_name',
                    'type': 'string',
                    'desc': 'the name\n  drives the process.\n'
                }
            ],
            'retmode': 'record',
            'retvals': [
                {
                    'source': '@retval contact_id: number - an identifier\n  to be returned.\n',
                    'name': 'contact_id',
                    'type': 'number',
                    'desc': 'an identifier\n  to be returned.\n'
                },
                {
                    'source': '@retval contact_name: string - the name,\nto be returned.\n',
                    'name': 'contact_name',
                    'type': 'string',
                    'desc': 'the name,\nto be returned.\n'
                }
            ],
        },
        'body': {
            'source': BODY
        }
    }
]
