import numpy as np
from secrets import token_bytes

def poly_uniform(seed, length):
    seed_32 = int.from_bytes(seed, 'big') % (2**32)
    np.random.seed(seed_32)
    return np.random.randint(-100, 100, length)

def poly_add(a, b):
    """Add two polynomials."""
    return (a + b) % 256

def poly_sub(a, b):
    """Subtract two polynomials."""
    return (a - b) % 256

def poly_mul(a, b):
    """Multiply two polynomials."""
    result = np.convolve(a, b) % 256
    return result[:len(a)]

if __name__ == "__main__":
    print(poly_uniform(token_bytes(32), 10))
    print(poly_add(np.array([1, 2, 3]), np.array([4, 5, 6])))
    print(poly_sub(np.array([1, 2, 3]), np.array([4, 5, 6])))
    print(poly_mul(np.array([1, 2, 3]), np.array([4, 5, 6])))

