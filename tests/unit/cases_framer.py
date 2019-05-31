from .utils import codeblock


CASES = (
    (
        "SingleComplexBlock",
        codeblock(
            """
            /**
            *
            * Retrieves some specific details about contacts matching the given name.
            *   This routine is safe to run in production.
            *
            * @dialect postgresql
            * @name add_contact
            * @param contact_name: string - the target contact's name
            * @retmode record
            * @retval name: string
            * @retval age: number
            * @retval created_at: datetime
            */
            {
                select * from contacts where name=%(name)s;
            }
            """
        ),
        [
            {
                "header": "Retrieves some specific details about contacts matching the given name.\n  This routine is safe to run in production.\n\n@dialect postgresql\n@name add_contact\n@param contact_name: string - the target contact's name\n@retmode record\n@retval name: string\n@retval age: number\n@retval created_at: datetime\n",  # noqa
                "body": "select * from contacts where name=%(name)s;\n"
            }
        ]
    ),

    # --------------------------------------------------------------------------------------------

    (
        "MultipleBlocks",
        codeblock(
            """
            /**
            * Description1
            */
            {
                body1
            }
            /**
            * Description2
            */
            {
                body2
            }
            """
        ),
        [
            {
                "header": "Description1\n",
                "body": "body1\n"
            },
            {
                "header": "Description2\n",
                "body": "body2\n"
            }
        ]
    ),

    # --------------------------------------------------------------------------------------------

    (
        "InvalidBlock",
        codeblock(
            """
            /*
            * Description
            */
            {
                body
            }
            """
        ),
        [
        ]
    ),

    # --------------------------------------------------------------------------------------------

    (
        "MixedInvalidBlock",
        codeblock(
            """
            /**
            * Valid Block
            */
            {
                body1
            }
            /*
            * Invalid Block
            */
            {
                body2
            }
            """
        ),
        [
            {
                "header": "Valid Block\n",
                "body": "body1\n"
            }
        ]
    ),

    # --------------------------------------------------------------------------------------------

    (
        "InlineBody",
        codeblock(
            """
            /**
            * Description
            */
            { body }
            """
        ),
        [
            {
                "header": "Description\n",
                "body": "body\n"
            }
        ]
    ),

    # --------------------------------------------------------------------------------------------

    (
        "BlankNewlineHeader",
        codeblock(
            """
            /**
            */
            { body }
            """
        ),
        [
            {
                "header": "",
                "body": "body\n"
            }
        ]
    ),


    # --------------------------------------------------------------------------------------------

    (
        "EmptyHeader",
        codeblock(
            """
            /***/
            { body }
            """
        ),
        [
            {
                "header": "",
                "body": "body\n"
            }
        ]
    ),

    # --------------------------------------------------------------------------------------------

    (
        "EmptyBody",
        codeblock(
            """
            /**
            * Description
            */
            { }
            """
        ),
        [
            {
                "header": "Description\n",
                "body": ""
            }
        ]
    ),
)
