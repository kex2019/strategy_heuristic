import strategy_heuristic.strategy_heuristic as sh
print("Starting evaluation")
sh.evaluate(
    render=True,
    robots=16+4+1,
    spawn=20,
    capacity=3,
    shelve_length=10,
    shelve_width=5,
    shelve_height=5,
    steps=10000,
    periodicity_lower=100,
    periodicity_upper=300,
    collect=True,
    even=True)
