from collections import namedtuple

Reward = namedtuple("Reward", "points chain_bonus mini_break")

POINTS_TABLE = {
    0: Reward(0, 0, 0),
    3: Reward(0.5, 1, 1),
    5: Reward(1, 1.1, 1),
    7: Reward(2, 1.2, 1),
    9: Reward(4, 1.3, 1),
    10: Reward(5, 1.4, 3),
    12: Reward(7, 1.5, 3),
    15: Reward(10, 1.6, 4),
    17: Reward(12.5, 1.7, 4),
    20: Reward(17, 1.8, 5),
    25: Reward(25, 1.9, 6),
    30: Reward(35, 2.0, 7),
    40: Reward(60, 2.1, 8),
    45: Reward(75, 2.2, 9),
    50: Reward(95, 2.3, 10),
    60: Reward(140, 2.4, 11),
}
