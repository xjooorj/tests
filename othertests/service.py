
database = {
    1: "oybek",
    2: "hilol",
    3: "zilol",
    
}

def get_user_from_db(user_id):
    return database.get(user_id)