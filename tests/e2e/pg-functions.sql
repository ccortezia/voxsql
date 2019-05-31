/**
 *
 * Adds a contact to the database, allows the name to be defined.
 *
 * @dialect postgresql
 * @name add_contact
 * @param contact_name: string - the target contact's name
 * @retmode record
 * @retval name: string
 */
{
    insert into contacts (name)
    values (%(contact_name)s)
    returning name
    ;
}

/**
 *
 * Adds a contact to the database, allows both the name and the age to be defined.
 *
 * @dialect postgresql
 * @name add_contact_details
 * @param contact_name: string - the target contact's name
 * @param age: number - the target contact's age
 * @retmode scalar
 * @retval name: id
 */
{
    insert into contacts (name, age)
    values (%(contact_name)s, %(age)s)
    returning id
    ;
}

/**
 *
 * Retrieves all contacts from the database.
 *
 * @dialect postgresql
 * @name list_contacts_as_records
 * @retmode records
 * @retval name: string
 * @retval age: number
 */
{
    select name, age from contacts;
}

/**
 *
 * Retrieves all contacts from the database.
 *
 * @dialect postgresql
 * @name list_contacts_as_tuples
 * @retmode tuples
 */
{
    select name, age from contacts;
}

/**
 *
 * Retrieves a contact's age from the database, selects by name.
 *
 * @dialect postgresql
 * @name get_contact_age_by_name
 * @param contact_name: string - the target contact's name
 * @retmode scalar
 */
{
    select age
    from contacts
    where name=%(contact_name)s
    ;
}
