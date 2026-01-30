import ccxt

def create_exchange(name):
    exchange = getattr(ccxt, name)({
        "enableRateLimit": True,
        "options": {"defaultType": "spot"}
    })
    exchange.set_sandbox_mode(True)
    return exchange
