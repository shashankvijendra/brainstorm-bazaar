from datetime import datetime, timedelta
data = {}
def rate_limit(customer_id, max_request_per_minute):
    limits = data.get(customer_id,[])
    while limits and limits[0] <= datetime.now()-timedelta(seconds=1):
        limits = limits[1:]
    limits.append(datetime.now())
    data[customer_id] = limits
    if limits and len(limits) > max_request_per_minute:
        return False
    return True

final = []
for i in range(10):
    final.append(rate_limit("customer1", 5))