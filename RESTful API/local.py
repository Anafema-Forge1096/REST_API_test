import requests


res = requests.get("http://127.0.0.1:3000/api/data/1")
#res = requests.delete("http://127.0.0.1:3000/api/data/2")
#res = requests.post("http://127.0.0.1:3000/api/data/4", {"name": "test test", "num": "00"})
#res = requests.put("http://127.0.0.1:3000/api/data/2", {"name": "test test", "num": "00"})
print(res.json())