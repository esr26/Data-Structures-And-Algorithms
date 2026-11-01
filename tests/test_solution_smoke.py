import contextlib
import io
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPICS = (
    "Array & Hashing",
    "Binary Search",
    "Bit Manupulation",
    "Graph",
    "Math",
    "Sliding Window",
    "Sorting",
    "Stacks",
    "Strings",
    "Two Pointers",
)


def load(relative_path):
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(str(ROOT / relative_path))


class SolutionSmokeTests(unittest.TestCase):
    def test_all_solutions_load(self):
        for topic in TOPICS:
            for path in (ROOT / topic).glob("*.py"):
                with self.subTest(path=str(path.relative_to(ROOT))):
                    load(path.relative_to(ROOT))

    def test_rewritten_array_algorithms(self):
        count = load("Array & Hashing/count inversion.py")["count_inversions"]
        self.assertEqual(count([2, 4, 1, 3, 5]), 3)
        self.assertEqual(count([]), 0)

        for filename in ("count subarrays with xor.py", "count subarrays with xor equals target.py"):
            xor_count = load(f"Array & Hashing/{filename}")["count_subarrays_with_xor"]
            self.assertEqual(xor_count([4, 2, 2, 6, 4], 6), 4)
            self.assertEqual(xor_count([], 0), 0)

        leaders = load("Array & Hashing/leaders in the array.py")["leaders_in_array"]
        self.assertEqual(leaders([16, 17, 4, 3, 5, 2]), [17, 5, 2])
        longest = load("Array & Hashing/longest subarray sum equal to 0.py")["longest_zero_sum_subarray"]
        self.assertEqual(longest([1, -1, 3, 2, -2, -3, 3]), 6)

    def test_search_and_in_place_update(self):
        bounds = load("Binary Search/floor and ceil in a sorted array.py")["floor_and_ceil"]
        self.assertEqual(bounds([1, 2, 4, 6], 5), [4, 6])
        self.assertEqual(bounds([], 5), [-1, -1])

        move = load("Two Pointers/move zeros to end.py")["Solution"]().moveZeroes
        nums = [0, 1, 0, 3, 12]
        self.assertIsNone(move(nums))
        self.assertEqual(nums, [1, 3, 12, 0, 0])

        duplicate = load("Array & Hashing/find duplicate number.py")["Solution"]().findDuplicate
        for values, expected in (([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3)):
            original = values.copy()
            self.assertEqual(duplicate(values), expected)
            self.assertEqual(values, original)

    def test_graph_helpers(self):
        moves = load("Graph/Minimum moves to each (m,n).py")["minimum_moves"]
        self.assertEqual(moves([[0, 0], [1, 0]]), 2)
        self.assertEqual(moves([[0]]), 0)
        self.assertEqual(moves([[0, 1], [1, 0]]), -1)
        self.assertEqual(moves([]), -1)

        bfs = load("Graph/Iterative BFS.py")["iterative_bfs"]
        self.assertEqual(bfs({"A": ["B", "C"], "B": ["C"]}, "A"), ["A", "B", "C"])

    def test_maximum_probability_path(self):
        solve = load("Graph/Path With Maximum Probability.py")["Solution"]().maxProbability
        edges = [[0, 1], [1, 2], [0, 2]]
        self.assertAlmostEqual(solve(3, edges, [0.5, 0.5, 0.2], 0, 2), 0.25)
        self.assertAlmostEqual(solve(3, edges, [0.5, 0.5, 0.3], 0, 2), 0.3)
        self.assertEqual(solve(3, [[0, 1]], [0.5], 0, 2), 0.0)
        self.assertEqual(solve(2, [[0, 1]], [0.0], 0, 1), 0.0)
        self.assertEqual(solve(1, [], [], 0, 0), 1.0)

    def test_shortest_alternating_paths(self):
        solve = load("Graph/Shortest Path With Alternating Colors.py")["Solution"]().shortestAlternatingPaths
        self.assertEqual(solve(3, [[0, 1], [1, 2]], []), [0, 1, -1])
        self.assertEqual(solve(3, [[0, 1]], [[1, 2]]), [0, 1, 2])
        self.assertEqual(solve(4, [[0, 1], [1, 2]], [[0, 1], [1, 3]]), [0, 1, 2, 2])
        self.assertEqual(solve(3, [[0, 1], [0, 2]], []), [0, 1, 1])
        self.assertEqual(solve(1, [], []), [0])

    def test_shortest_path_with_obstacle_elimination(self):
        solve = load("Graph/Shortest Path in a Grid with Obstacles Elimination.py")["Solution"]().shortestPath
        self.assertEqual(solve([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1), 6)
        self.assertEqual(solve([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1), -1)
        self.assertEqual(solve([[0, 0, 1], [1, 0, 1], [1, 1, 0]], 1), 4)
        self.assertEqual(solve([[0, 1, 0], [1, 1, 0]], 1), 3)
        self.assertEqual(solve([[0]], 0), 0)

    def test_missing_import_regressions(self):
        self.assertEqual(load("Graph/01 Matrix.py")["Solution"]().updateMatrix([[0, 1], [1, 1]]), [[0, 1], [1, 2]])
        self.assertEqual(load("Graph/Print Shortest Path.py")["Solution"]().shortestPath(3, 2, [[1, 2, 2], [2, 3, 3]]), [5, 1, 2, 3])
        self.assertEqual(load("Graph/Shortest Path in Binary Matrix.py")["Solution"]().shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
        ladders = load("Graph/Word Ladder II.py")["Solution"]().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        self.assertEqual({tuple(path) for path in ladders}, {("hit", "hot", "dot", "dog", "cog"), ("hit", "hot", "lot", "log", "cog")})

        self.assertTrue(load("Sliding Window/permutation string.py")["Solution"]().checkInclusion("ab", "eidbaooo"))
        self.assertEqual(load("Sliding Window/sliding-window-maximum.py")["Solution"]().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(load("Strings/sort-characters-by-frequency.py")["Solution"]().frequencySort("tree"), "eetr")

        time_map = load("Binary Search/time based key value search.py")["TimeMap"]()
        time_map.set("foo", "bar", 1)
        self.assertEqual(time_map.get("foo", 3), "bar")
        stack = load("Stacks/implement-stack-using-queues.py")["MyStack"]()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        frequency_stack = load("Stacks/maximum-frequency-stack.py")["FreqStack"]()
        for value in (5, 7, 5, 7, 4, 5):
            frequency_stack.push(value)
        self.assertEqual(frequency_stack.pop(), 5)

    def test_empty_input_guards(self):
        self.assertEqual(load("Array & Hashing/longest common prefix.py")["Solution"]().longestCommonPrefix([]), "")
        self.assertEqual(load("Array & Hashing/spiral matrix.py")["Solution"]().spiralOrder([]), [])
        matrix = []
        self.assertIsNone(load("Array & Hashing/set matrix zeros.py")["Solution"]().setZeroes(matrix))
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.assertIsNone(load("Array & Hashing/set matrix zeros.py")["Solution"]().setZeroes(matrix))
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        self.assertEqual(load("Sliding Window/best-time-to-buy-and-sell-stock.py")["Solution"]().maxProfit([]), 0)
        for filename in ("Search a 2D Matrix II.py", "search in 2d matrix.py"):
            self.assertFalse(load(f"Binary Search/{filename}")["Solution"]().searchMatrix([], 1))
        self.assertEqual(load("Binary Search/Find a Peak Element II.py")["Solution"]().findPeakGrid([]), [-1, -1])
        self.assertEqual(load("Binary Search/Find a Peak Element II.py")["Solution"]().findPeakGrid([[-5]]), [0, 0])
        self.assertEqual(load("Binary Search/minimum gas stations.py")["Solution"]().minmaxGasDist([1], 2), 0.0)
        self.assertAlmostEqual(load("Binary Search/minimum gas stations.py")["Solution"]().minmaxGasDist([0, 10], 1), 5.0, places=5)


if __name__ == "__main__":
    unittest.main()
