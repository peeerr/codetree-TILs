class Agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = int(score)

agents = sorted([Agent(*input().split()) for _ in range(5)], key=lambda x : x.score)

print(agents[0].code_name, agents[0].score)