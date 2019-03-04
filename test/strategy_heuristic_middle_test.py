import strategy_heuristic.strategy_heuristic as sh
print("Starting evaluation")
sh.evaluate(
    render=True,
    robots=8,
    spawn=20,
    capacity=3,
    shelve_length=2,
    shelve_width=4,
    shelve_height=4,
    steps=10000,
    periodicity_lower=200,
    periodicity_upper=500,
    collect=True)
