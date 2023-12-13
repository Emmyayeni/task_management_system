import re
import json

json_text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

# Parse the JSON
data = json.loads(json_text)
yellow_id_values = [entry["id"] for entry in data.get("orders", [])]

code_values = [entry["code"] for entry in data.get("errors", [])]

print("Yellow ID values:", yellow_id_values)
print("Code values:", code_values)
