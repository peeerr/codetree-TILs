class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

secret = Secret(*input().split())

print(f"secret code : {secret.code}")
print(f"meeting point : {secret.place}")
print(f"time : {secret.time}")