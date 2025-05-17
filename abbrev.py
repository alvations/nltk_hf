import math

def dunning_log_likelihood(count_a, count_b, count_ab, N):
    """
    Calculates the modified Dunning log-likelihood ratio score for determining
    whether a token and a following period (e.g., 'Dr.') form a single unit,
    as opposed to occurring independently (e.g., 'Dr .' with a space).

    Parameters:
        count_a (int): Total occurrences of the token with and without the period.
        count_b (int): Total occurrences of period tokens in the corpus.
        count_ab (int): Occurrences of the token followed immediately by a period.
        N (int): Total number of tokens in the corpus.

    Returns:
        float: Dunning log-likelihood score — higher values indicate stronger
               association between the token and the period (more likely to be
               a single unit like an abbreviation).
    """
    if N <= 0:
        raise ValueError("Total number of observations N must be greater than 0.")
    if not (0 <= count_ab <= count_a and 0 <= count_b <= N):
        raise ValueError("Invalid count relationships among inputs.")

    # Small constant to avoid log(0)
    epsilon = 1e-10
    p1 = count_b / N  # Empirical probability of a period
    p2 = 0.99         # Hypothesized probability if token+period is a true unit

    # Log-likelihood under the null hypothesis (independent occurrences)
    null_hypo = (
        count_ab * math.log(max(p1, epsilon)) +
        (count_a - count_ab) * math.log(max(1.0 - p1, epsilon))
    )
    # Log-likelihood under the alternative hypothesis (true unit)
    alt_hypo = (
        count_ab * math.log(p2) +
        (count_a - count_ab) * math.log(1.0 - p2)
    )

    likelihood_ratio = null_hypo - alt_hypo
    return max(0.0, -2.0 * likelihood_ratio)
