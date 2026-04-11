# alchemical_uncertainty.py - MIT License
import numpy as np

def alchemical_uncertainty(data, manifold):
    """Quantifies uncertainty: if >0.75 → revenue trigger"""
    delta_geom = np.linalg.norm(data - manifold) / len(manifold)
    beta = len([p for p in manifold[0] if p[0] > 0.5])  # Topological entropy
    return float(delta_geom * beta), delta_geom + (beta * 0.1) >= 0.75

# Usage:
# is_violated, _ = alchemical_uncertainty(user_input, system_data)
