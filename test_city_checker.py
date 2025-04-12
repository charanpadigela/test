import unittest
from collections import deque

def are_connected(graph, city1, city2):
    if city1 not in graph or city2 not in graph:
        return False
    visited = set()
    queue = deque([city1])
    while queue:
        current = queue.popleft()
        if current == city2:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False

class TestCityConnections(unittest.TestCase):

    def setUp(self):
        # Build the graph from the given city pairs
        self.graph = {
            "New York": {"Los Angeles"},
            "Los Angeles": {"New York"},
            "Chicago": {"San Diego"},
            "San Diego": {"Chicago"},
            "Columbus": {"Las Vegas"},
            "Las Vegas": {"Columbus"}
        }

    def test_connected_ny_la(self):
        self.assertTrue(are_connected(self.graph, "New York", "Los Angeles"))

    def test_connected_columbus_lv(self):
        self.assertTrue(are_connected(self.graph, "Columbus", "Las Vegas"))

    def test_connected_chicago_sd(self):
        self.assertTrue(are_connected(self.graph, "Chicago", "San Diego"))

    def test_not_connected_ny_chicago(self):
        self.assertFalse(are_connected(self.graph, "New York", "Chicago"))

    def test_not_connected_sd_lv(self):
        self.assertFalse(are_connected(self.graph, "San Diego", "Las Vegas"))

    def test_same_city(self):
        self.assertTrue(are_connected(self.graph, "New York", "New York"))

if _name_ == "_main_":
    unittest.main()