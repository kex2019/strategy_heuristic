import strategy_heuristic.strategy_heuristic as sh
print("Starting evaluation")
sh.evaluate(
    render=True,
    robots=6,
    spawn=20,
    capacity=3,
    shelve_length=5,
    shelve_width=2,
    shelve_height=2,
    steps=10000,
    periodicity_lower=100,
    periodicity_upper=300,
    collect=True)
