def single(obj, tableName, clause, clauseValue):
    if (clause == "id") | (clause == "ES") | (clause == "US") | (clause == "MX") | (clause == "CO") | (clause == "special") :
        query = (
            "SELECT {} FROM `{}` WHERE {} = {}"
            .format(obj, tableName, clause, clauseValue)
        )
        return query
    elif (clause == "url") | (clause == "site") | (clause == "type") | (clause == "published") :
        query = (
            "SELECT {} FROM `{}` WHERE {} = '{}'"
            .format(obj, tableName, clause, clauseValue)
        )
        return query
    elif (clause == "publishedGreaterThan"):
        query = (
            "SELECT {} FROM `{}` WHERE published > '{}'"
            .format(obj, tableName, clauseValue)
        )
        return query
    elif (clause == "publishedLessThan"):
        query = (
            "SELECT {} FROM `{}` WHERE published < '{}'"
            .format(obj, tableName, clauseValue)
        )
        return query

def collection(obj, tableName, whereClauses, limit, offset):
    query = []
    
    for clause in whereClauses:
        if type(clause[2]) is str:
            query.append(" {} {} '{}'".format(clause[0], clause[1], clause[2]))
        else:
            query.append(" {} {} {}".format(clause[0], clause[1], clause[2]))
    query = " AND".join(query)

    query = "SELECT {} FROM `{}` WHERE ".format(obj, tableName) + query
    query = query + " LIMIT {} OFFSET {}".format(limit, offset)
    return query