class Address:
    def __init__(self, name, street_number, region):
        self.name = name
        self.street_number = street_number
        self.region = region

n = int(input())
res = sorted([Address(*input().split()) for _ in range(n)], key=lambda x : x.name)[-1]

print(f"name {res.name}")
print(f"addr {res.street_number}")
print(f"city {res.region}")