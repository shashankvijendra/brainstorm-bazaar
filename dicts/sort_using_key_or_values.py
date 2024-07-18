test_dict = {"Gfg": 5, "is": 7, "Best": 2, "for": 9, "geeks": 8}
print("Original dictionary:", test_dict)

# Sort by keys in ascending order
res = {key: val for key, val in sorted(test_dict.items(), key=lambda ele: ele[0])}
print("Result dictionary sorted by keys:", res)

# Sort by keys in reversed order
res_reversed = {key: val for key, val in sorted(test_dict.items(), key=lambda ele: ele[0], reverse=True)}
print("Result dictionary sorted by keys (in reversed order):", res_reversed)
