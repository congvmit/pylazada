from .base import LazClient, LazRequest

# TODO:
client = LazClient("https://api.lazada.vn/rest", CLIENT_ID, CLIENT_SECRET)
request = LazRequest("/orders/items/get", "GET")


order_ids = []


order_items = []
batch = 50

for i in range(0, len(order_ids), batch):
    request.add_api_param("order_ids", str(order_ids[i : i + batch]))
    response = client.execute(request, ACCESS_TOKEN)

    if "message" in response.body:
        message = response.body["message"]
        raise Exception(f"Broken get_order_items API, message: {message}")

    for resp in response.body["data"]:
        order_items.extend(resp["order_items"])
