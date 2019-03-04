import strategy_heuristic.strategy_heuristic as sh
print("Starting evaluation")
sh.evaluate(
    render=True,
    robots=21,
    spawn=20,
    capacity=1,
    shelve_length=2,
    shelve_width=5,
    shelve_height=5,
    steps=10000,
    periodicity_lower=300,
    periodicity_upper=500,
    collect=True,
    even=True)
