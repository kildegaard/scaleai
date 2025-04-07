class LargestPrime {
    public static void main(String[] args) {
        int n = 1000000000; // Example input
        int largestPrime = findLargestPrime(n);
        if (largestPrime != -1) {
            System.out.println("The largest prime number less than " + n + " is " + largestPrime);
        } else {
            System.out.println("There is no prime number less than " + n);
        }
    }

    // Function to find the largest prime number less than n
    public static int findLargestPrime(int n) {
        for (int i = n - 1; i > 1; i--) {
            if (isPrime(i)) {
                return i;
            }
        }
        return -1;
    }

    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
