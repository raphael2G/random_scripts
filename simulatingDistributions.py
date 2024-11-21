import numpy as np

def generate_geometric_samples(p, n_samples):
    """
    Generate random samples from a Geometric(p) distribution.

    Parameters:
        p (float): Probability of success on each trial (0 < p < 1).
        n_samples (int): Number of samples to generate.

    Returns:
        np.ndarray: Array of generated Geometric(p) random variables.
    """
    if not (0 < p < 1):
        raise ValueError("Probability p must be between 0 and 1.")

    # Generate uniform random variables
    U = np.random.uniform(0, 1, n_samples)

    # Apply the inverse transform method
    k = np.ceil(np.log(U) / np.log(1 - p)).astype(int)

    return k

def main():
    # Parameters
    p = 0.2
    n_samples = 50

    # Generate samples
    samples = generate_geometric_samples(p, n_samples)

    # Compute the sample mean
    sample_mean = np.mean(samples)

    # Theoretical mean of the Geometric distribution
    theoretical_mean = 1 / p

    # Display the results
    print("Generated Samples:")
    print(samples)
    print(f"\nSample Mean: {sample_mean:.2f}")
    print(f"Theoretical Mean: {theoretical_mean:.2f}")
    print(f"\nDifference between Sample Mean and Theoretical Mean: {abs(sample_mean - theoretical_mean):.2f}")

if __name__ == "__main__":
    main()
