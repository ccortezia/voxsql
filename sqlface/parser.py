

def parse_file_content(text):
    pass


def parse_query(text):
    pass


def parse_query_header(text):
    pass

# scan lines
# find comment block anchor
# find comment block terminating boundary
# extract payload documentation by discarding comment tokens
# extract description segment => r".*?(@type|@name|@param|@return)"/ms
# extract @type segment => r"@type\s+(dql|DQL|ddl|DDL|dml|DML)"
# extract @name segment => r"@name\s+(.*)(@param|@return)?"
# extract @param segment => r"@param\s+([a-zA-Z]+):\s+([a-zA-Z\[\]]+)"/g
# extract @return segment => r"@return\s*(.*)"/s
