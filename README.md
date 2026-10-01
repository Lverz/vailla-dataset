# Vailla Dataset

Vailla is an abstract reasoning and graph-based thinking dataset designed for training models that must reason over concepts, systems, theories, and causal structures rather than only surface-level facts.

## Contents

- `data/train.jsonl`: starter training set with abstract reasoning tasks
- `data/validation.jsonl`: small validation set
- `data/schema.json`: dataset schema definition
- `scripts/generate_vailla_dataset.py`: generator for expanding the dataset to large scale

## Dataset focus

- abstract problem solving
- graph-based reasoning
- theory-grounded inference
- causal and semantic dependency analysis
- contradiction, emergence, and systems thinking

## Example record

```json
{
  "id": "vailla_000001",
  "domain": "dialectics",
  "category": "abstract_reasoning",
  "difficulty": "medium",
  "prompt": "A thesis intensifies local cohesion while an antithesis introduces disruption. If both persist, what is the most likely result?",
  "graph": {
    "nodes": [
      {"id": "t", "label": "thesis", "type": "state"},
      {"id": "a", "label": "antithesis", "type": "state"},
      {"id": "s", "label": "synthesis", "type": "state"}
    ],
    "edges": [
      {"from": "t", "to": "s", "relation": "contributes_to"},
      {"from": "a", "to": "s", "relation": "forces"},
      {"from": "t", "to": "a", "relation": "opposes"}
    ]
  },
  "reasoning_steps": [
    "The thesis and antithesis are in tension.",
    "Their opposition creates pressure for restructuring.",
    "A synthesis emerges when conflict is resolved into a new stable form."
  ],
  "answer": "The system tends toward a synthesis that preserves useful structure while absorbing the disruption.",
  "metadata": {
    "theory_tags": ["dialectics", "contradiction", "systems"],
    "reasoning_type": ["graph_based", "multi_step"],
    "language": "en"
  }
}
```

## Expansion

The generator script can generate many more samples using theory templates and graph construction rules. Run:

```bash
python scripts/generate_vailla_dataset.py --count 10000 --output data/train.jsonl
```

This is intentionally designed for abstract, graph-based reasoning rather than factual recall.
