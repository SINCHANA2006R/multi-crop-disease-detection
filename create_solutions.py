import json

# -------------------
# Load class labels from class_indices.json
# -------------------
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)

# Reverse mapping (index -> class name)
idx_to_class = {v: k for k, v in class_indices.items()}

# -------------------
# Build disease_solutions.json
# -------------------
disease_solutions = {}
for _, class_name in idx_to_class.items():
    disease_solutions[class_name] = {
        "organic": f"Organic solution for {class_name} (edit me)",
        "inorganic": f"Inorganic solution for {class_name} (edit me)"
    }

# Save to JSON
with open("disease_solutions.json", "w") as f:
    json.dump(disease_solutions, f, indent=4)

print("✅ Created disease_solutions.json. Now edit it to add real solutions.")