
SOURCE = """/**
 *
 * Do something amazing but try not to destroy the entire database
 *   in the process.
 *
 * Anytime something comes up, raises an error.
 *
 * @dialect postgresql
 * @name add_contact
 * @param contact_name: string - the name
 * @retmode record
 * @retval contact_id: number
 * @retval contact_name: string
 */
{
    insert into contacts (name)
    values (%(contact_name)s)
    returning id, name
    ;
}
"""

HEADER = """Do something amazing but try not to destroy the entire database
  in the process.

Anytime something comes up, raises an error.

@dialect postgresql
@name add_contact
@param contact_name: string - the name
@retmode record
@retval contact_id: number
@retval contact_name: string
"""

HEADER_DESC = """Do something amazing but try not to destroy the entire database
  in the process.

Anytime something comes up, raises an error.
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
                    'source':  '@param contact_name: string - the name\n',
                    'name': 'contact_name',
                    'type': 'string',
                    'desc': 'the name\n'
                }
            ],
            'retmode': 'record',
            'retvals': [
                {
                    'source':  '@retval contact_id: number\n',
                    'name': 'contact_id',
                    'type': 'number',
                    'desc': ''
                },
                {
                    'source':  '@retval contact_name: string\n',
                    'name': 'contact_name',
                    'type': 'string',
                    'desc': ''
                }
            ],
        },
        'body': {
            'source': BODY
        }
    }
]
