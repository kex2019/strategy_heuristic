import strategy_heuristic.strategy_heuristic as sh
print("Starting evaluation")
sh.evaluate(
    render=True,
    robots=85,
    spawn=200,
    capacity=1,
    shelve_length=2,
    shelve_width=10,
    shelve_height=10,
    steps=10000,
    periodicity_lower=300,
    periodicity_upper=500,
    collect=True,
    even=True)
