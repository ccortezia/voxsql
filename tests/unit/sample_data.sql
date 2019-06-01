/**
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
