class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

spy = Spy(*input().split())

print(f"secret code : {spy.secret_code}")
print(f"meeting point : {spy.meeting_point}")
print(f"time : {spy.time}")