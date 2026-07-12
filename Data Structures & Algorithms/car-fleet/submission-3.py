class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = map(list, zip(*sorted(zip(position,speed))))

        numFleets = 0
        time2arrival = []
        for p,s in zip(position,speed):
            time2arrival.append((float(target)-float(p))/float(s))

        leadertime = 0

        while time2arrival:
            time = time2arrival.pop()
            if time > leadertime:
                numFleets += 1
            leadertime = max(leadertime, time)

        return numFleets