# Data Structures and Algorithms

Python solutions are grouped by topic. Each topic folder has a `NOTES.md` with a short workflow, complexity, and common mistakes.

## Study workflow

1. Pick a topic from [the tracker](DSA%20Tracker.xlsx) or the [two-week study plan](agent_output/agent_e_gaps_study_plan.md).
2. Read that topic's `NOTES.md`, then solve a problem before opening its `.py` file.
3. Record mistakes and review dates in the tracker. `Solved` means a solution has been recorded; it does not certify correctness. Blank LeetCode numbers and difficulties are marked `NEEDS REVIEW` in the notes column.
4. Use the [visual prompts](visual_prompts/) to make algorithm infographics when a pattern is hard to remember.

The tracker uses `Arrays` for the `Array & Hashing` folder. Other topic tabs match their folder names, including the existing `Bit Manupulation` spelling.

## Repo checks

Run the smoke tests with Python 3.13 (the version used for verification):

```sh
python -B -m unittest discover -s tests -v
```

The tests load every solution and exercise repaired algorithms and imports. They are a starting check, not a full proof for every problem. The [solution review](agent_output/agent_b_solution_review.md) records the initial audit; the [remediation summary](agent_output/remediation_summary.md) records subsequent fixes and remaining work.
