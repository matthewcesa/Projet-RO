# generate_inputs.py

for p in range(1, 13):
    for algo, name in [(1, "no"), (2, "bh")]:
        filename = f"input{p}-{name}.txt"
        with open(filename, "w") as f:
            f.write(f"{p}\n{algo}\n0\n")
