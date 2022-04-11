import json

test = b'{"data":{"id":"1513413325731868675","text":"test"},"matching_rules":[{"id":"1513413238276472837","tag":"Meisinger2"}]}'

#print(test.decode('UTF-8'))

remove_b = test.decode('UTF-8')

y = json.loads(remove_b)

print(y["data"]["text"])
print(y["matching_rules"][0]["tag"])