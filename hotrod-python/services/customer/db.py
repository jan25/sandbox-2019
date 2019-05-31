

customers = {
    "123": {
        'ID':       "123",
        'Name':     "Rachel's Floral Designs",
        'Location': "115,277",
    },
    "567": {
        'ID':       "567",
        'Name':     "Amazing Coffee Roasters",
        'Location': "211,653",
    },
    "392": {
        'ID':       "392",
        'Name':     "Trom Chocolatier",
        'Location': "577,322",
    },
    "731": {
        'ID':       "731",
        'Name':     "Japanese Deserts",
        'Location': "728,326",
    },
}

def get_customer_by_id(customer_id):
    if customer_id not in customers:
        # TODO add logs here
        return
    return customers[customer_id]
