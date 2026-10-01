#!/usr/bin/env python3
import json
import random
from pathlib import Path

THEORY_LIBRARY = {
    "dialectics": {
        "prompt": "A thesis and antithesis conflict while a synthesis emerges from their tension.",
        "entities": ["thesis", "antithesis", "synthesis"],
        "relations": [
            ("thesis", "antithesis", "opposes"),
            ("thesis", "synthesis", "contributes_to"),
            ("antithesis", "synthesis", "forces")
        ],
        "reasoning": [
            "The thesis and antithesis are in direct opposition.",
            "The conflict creates pressure for a new arrangement.",
            "The synthesis absorbs the strengths of each while reducing the tension."
        ],
        "answer": "The system resolves into a synthesis that integrates the valuable aspects of the opposing forces."
    },
    "systems_theory": {
        "prompt": "A feedback loop strengthens one component while a balancing process resists it.",
        "entities": ["reinforcing_loop", "balancing_loop", "equilibrium"],
        "relations": [
            ("reinforcing_loop", "equilibrium", "moves_toward"),
            "balancing_loop",
            "equilibrium"
        ],
        "reasoning": [
            "The reinforcing loop pushes the system away from stasis.",
            "The balancing loop applies corrective pressure.",
            "The eventual state is a negotiated equilibrium rather than pure collapse or pure growth."
        ],
        "answer": "The system settles into a dynamic equilibrium where both forces remain active but no longer dominate the whole."
    },
    "epistemology": {
        "prompt": "A model is updated by evidence that contradicts earlier assumptions.",
        "entities": ["prior_model", "evidence", "revised_model"],
        "relations": [
            ("prior_model", "evidence", "is_challenged_by"),
            ("evidence", "revised_model", "supports"),
            ("prior_model", "revised_model", "transforms_into")
        ],
        "reasoning": [
            "The prior model is not rejected instantly; it is challenged by anomalies.",
            "Evidence provides a basis for restructuring the model.",
            "The revised model becomes more reliable by integrating the contradiction."
        ],
        "answer": "Knowledge advances through revision: the model changes shape when evidence exposes a contradiction."
    },
    "causality": {
        "prompt": "A causal chain includes a trigger, a mediator, and an outcome.",
        "entities": ["trigger", "mediator", "outcome"],
        "relations": [
            ("trigger", "mediator", "activates"),
            ("mediator", "outcome", "produces")
        ],
        "reasoning": [
            "The trigger alone does not determine the outcome.",
            "The mediator converts the initial signal into a systemic consequence.",
            "The final effect depends on the interaction of both layers."
        ],
        "answer": "The outcome emerges from an intermediate causal process rather than from the trigger alone."
    },
    "emergence": {
        "prompt": "Local interactions among multiple agents produce a shared pattern across the whole system.",
        "entities": ["agent_a", "agent_b", "collective_pattern"],
        "relations": [
            ("agent_a", "collective_pattern", "contributes_to"),
            ("agent_b", "collective_pattern", "contributes_to")
        ],
        "reasoning": [
            "Individual actions are local, partial, and not identical.",
            "Their combined behavior produces a higher-order structure.",
            "The collective pattern is not reducible to a single agent."
        ],
        "answer": "A higher-order pattern emerges from localized interaction, yielding behavior that cannot be attributed to one agent alone."
    },
    "topology": {
        "prompt": "A network contains two paths from source to target; one path is shorter but more fragile.",
        "entities": ["source", "path_a", "path_b", "target"],
        "relations": [
            ("source", "path_a", "leads_to"),
            ("path_a", "target", "connects"),
            ("source", "path_b", "leads_to"),
            ("path_b", "target", "connects")
        ],
        "reasoning": [
            "Multiple routes exist between source and target.",
            "The shorter route offers efficiency but higher dependence on one node.",
            "The longer route is slower but more resilient under perturbation."
        ],
        "answer": "The network remains functional through redundancy, even though the short path is faster and the long path is more robust."
    }
}


def make_graph(domain_name, template):
    nodes = []
    edges = []
    for idx, entity in enumerate(template["entities"]):
        nodes.append({"id": f"n{idx}", "label": entity, "type": "concept"})
    for idx, rel in enumerate(template["relations"]):
        if isinstance(rel, tuple):
            a, b, r = rel
            if a in template["entities"] and b in template["entities"]:
                edges.append({
                    "from": a,
                    "to": b,
                    "relation": r
                })
    return {"nodes": nodes, "edges": edges}


def make_prompt(domain_name, template):
    return template["prompt"]


def build_sample(domain_name, idx):
    template = THEORY_LIBRARY[domain_name]
    graph = make_graph(domain_name, template)
    prompt = make_prompt(domain_name, template)
    reasoning_steps = list(template["reasoning"])
    answer = template["answer"]
    metadata = {
        "theory_tags": [domain_name, "abstract_reasoning"],
        "reasoning_type": ["graph_based", "multi_step"],
        "language": "en"
    }
    return {
        "id": f"vailla_{idx:06d}",
        "domain": domain_name,
        "category": "abstract_reasoning",
        "difficulty": random.choice(["easy", "medium", "hard", "expert"]),
        "prompt": prompt,
        "graph": graph,
        "reasoning_steps": reasoning_steps,
        "answer": answer,
        "metadata": metadata,
    }


def generate_dataset(count: int, output_path: str):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    domain_names = list(THEORY_LIBRARY.keys())
    samples = []
    for i in range(count):
        domain = random.choice(domain_names)
        samples.append(build_sample(domain, i + 1))

    with path.open("w", encoding="utf-8") as fh:
        for sample in samples:
            fh.write(json.dumps(sample, ensure_ascii=False) + "\n")

    print(f"Generated {count} samples to {path}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Vailla abstract reasoning dataset")
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--output", type=str, default="data/train.jsonl")
    args = parser.parse_args()
    generate_dataset(args.count, args.output)
