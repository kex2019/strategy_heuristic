import strategy_heuristic.strategy_heuristic as sh
print("Starting evaluation")
sh.evaluate(
    render=True,
    robots=84,
    spawn=100,
    capacity=1,
    shelve_length=4,
    shelve_width=10,
    shelve_height=10,
    steps=10000,
    periodicity_lower=100,
    periodicity_upper=700,
    collect=True,
    even=True)
