
SOURCE = """/**
 *
 * Do something
 *
 * @dialect postgresql
 * @name get_contacts
 * @param contact_name: string - the name
 * @param contact_origin: string - the origin
 * @retmode tuples
 *
{
    select * from contacts
    where name=%(contact_name)s and origin=%(contact_origin)s
    ;
}
"""

FRAMES = []
