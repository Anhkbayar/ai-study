import random

class VacuumEnvironment:
    def __init__(self):
        self.rooms = {
            "A": random.randint(0, 5),
            "B": random.randint(0, 5),
            "C": random.randint(0, 7),
            "D": random.randint(0, 3)
        }
        self.order = ["A", "B", "C", "D"]
        self.agent_location = "A"

    def percept(self):
        return (self.agent_location, self.rooms[self.agent_location])

    def execute_action(self, action):
        idx = self.order.index(self.agent_location)

        if action == "Suck":
            if self.rooms[self.agent_location] > 0:
                self.rooms[self.agent_location] -= 1
                print(f"{self.agent_location} uruug tseverlesen. (Bohir uruunuud: {self.rooms[self.agent_location]})")
            else:
                print(f"{self.agent_location} tseverlsen baina.")

        elif action == "Left":
            if idx > 0:
                self.agent_location = self.order[idx - 1]
                print(f"Toos sorogch {self.agent_location} uruu luu yvsan.")
            else:
                print("Zuun yvj bolohgui.")

        elif action == "Right":
            if idx < len(self.order) - 1:
                self.agent_location = self.order[idx + 1]
                print(f"Toos sorogch {self.agent_location} uruu luu yvsan.")
            else:
                print("Baruun hudulj bolohgui.")

        elif action == "NoOp":
            print("Toos sorogch zorilgodoo hursen.")

    def status(self):
        return self.rooms


class VacuumCleaner:
    def __init__(self, goal, energy=10):
        self.goal = goal
        self.energy = energy
        self.total_actions = 0
        self.order = ["A", "B", "C", "D"]

    def program(self, percept, env_status):
        location, dirt_level = percept

        if env_status == self.goal or self.energy <= 0:
            return "NoOp"

        if dirt_level > 0:
            return "Suck"

        idx = self.order.index(location)
        if idx < len(self.order) - 1:
            return "Right"
        else:
            return "Left"


if __name__ == "__main__":
    env = VacuumEnvironment()
    goal = {"A": 0, "B": 0, "C": 0, "D": 0}
    agent = VacuumCleaner(goal, energy=12)

    print("Toos sorogchiin zorilgo:", goal)
    print("Uruunuudiin baidal:", env.status())
    print("Toos sorogchiin battery:", agent.energy)

    while env.status() != goal and agent.energy > 0:
        percept = env.percept()
        action = agent.program(percept, env.status())

        print(f"\nPercept={percept} | Action={action}")

        env.execute_action(action)

        if action != "NoOp":
            agent.energy -= 1
            agent.total_actions += 1

        print(f"Orchin: {env.status()} | Uldsen battery={agent.energy}")

        if action == "NoOp":
            break

    print("\nDaalgvr duussan.")
    print("Niit hiisen uildel:", agent.total_actions)
    print("Geriin baidal:", env.status())
