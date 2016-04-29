def single(selectProperty, tableName, clause):
    query = "SELECT {} FROM `{}` WHERE ".format(selectProperty, tableName)
    if type(clause[2]) is str:
        query += " {} {} '{}'".format(clause[0], clause[1], clause[2])
    else:
        query += " {} {} {}".format(clause[0], clause[1], clause[2])
    return query

def collection(selectProperty, tableName, whereClauses, queryRange, limit):
    query = []
    
    for clause in whereClauses:
        if type(clause[2]) is str:
            query.append(" {} {} '{}'".format(clause[0], clause[1], clause[2]))
        else:
            query.append(" {} {} {}".format(clause[0], clause[1], clause[2]))
    query.append(" id >= {}".format(queryRange))
    query = " AND".join(query)


    query = "SELECT {} FROM `{}` WHERE ".format(selectProperty, tableName) + query
    query = query + " LIMIT {}".format(limit)
    return query