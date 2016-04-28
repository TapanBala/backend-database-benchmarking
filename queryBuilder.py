def single(property, tableName, clause):
    query = "SELECT {} FROM `{}` WHERE ".format(property, tableName)
    if type(clause[2]) is str:
        query += " {} {} '{}'".format(clause[0], clause[1], clause[2])
    else:
        query += " {} {} {}".format(clause[0], clause[1], clause[2])
    return query

def collection(property, tableName, whereClauses, limit, offset):
    query = []
    
    for clause in whereClauses:
        if type(clause[2]) is str:
            query.append(" {} {} '{}'".format(clause[0], clause[1], clause[2]))
        else:
            query.append(" {} {} {}".format(clause[0], clause[1], clause[2]))
    query = " AND".join(query)

    query = "SELECT {} FROM `{}` WHERE ".format(property, tableName) + query
    query = query + " LIMIT {} OFFSET {}".format(limit, offset)
    return query