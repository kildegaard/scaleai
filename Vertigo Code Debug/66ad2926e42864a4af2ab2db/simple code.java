import java.util.BitSet;

class LargestPrimeOptimized {
    public static void main(String[] args) {
        int n = 1000000000; // Example input
        int largestPrime = findLargestPrime(n);
        if (largestPrime != -1) {
            System.out.println("The largest prime number less than " + n + " is " + largestPrime);
        } else {
            System.out.println("There is no prime number less than " + n);
        }
    }

    public static int findLargestPrime(int n) {
        if (n <= 2) {
            return -1; // No prime numbers less than 2
        }

        // Initialize a BitSet for odd numbers only
        BitSet isPrime = new BitSet((n + 1) / 2);
        isPrime.set(0, isPrime.size(), true); // Assume all numbers are prime
        isPrime.clear(0); // 1 is not a prime number

        // Cross out non-prime numbers
        int sqrtN = (int) Math.sqrt(n) + 1;
        for (int i = 3; i <= sqrtN; i += 2) {
            if (isPrime.get(i / 2)) {
                for (int j = i * i; j < n; j += 2 * i) {
                    isPrime.clear(j / 2);
                }
            }
        }

        // Find the largest prime number less than n
        for (int i = (n - 1) | 1; i >= 3; i -= 2) {
            if (isPrime.get(i / 2)) {
                return i;
            }
        }

        return 2; // If no prime found, return 2 as the largest prime less than n
    }
}
