import pytest
import numpy as np
from core.population import evaluate_fitness
from benchmark.sphere import sphere


# Creates a dummy solution vector
@pytest.mark.parametrize("solution", [
    [1, 0.0, 3],
    [1.0, 2.0, 3.0],
    [0.0, 0.0, 0.0],
    [-1.0, 2.5, -3.7],
    np.array([4.0, 5.0, 6.0]),
])
def test_evaluate_fitness(solution):
    # Passes it to evaluate_fitness using the sphere function
    result = evaluate_fitness(solution, sphere)

    assert isinstance(result, float)
    assert not isinstance(result, list)
    assert not isinstance(result, np.ndarray)
