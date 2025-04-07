import java.util.Arrays;
import java.util.Collections;
import java.util.List;

// public class ShuffleArray2 {
//     public static void main(String[] args) {
//         Integer[] array = { 1, 2, 3, 4, 5 };

//         // Convert the array to a List
//         List<Integer> list = Arrays.asList(array);

//         // Shuffle the list using the Collections.shuffle() method
//         Collections.shuffle(list);

//         // Convert the list back to an array (if needed)
//         list.toArray(array);

//         // Print the shuffled array
//         System.out.println(Arrays.toString(array));
//     }
// }

import java.util.Random;

public class ShuffleArray2 {
    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4, 5 };

        // Create a Random object for generating random indices
        Random random = new Random();

        // Iterate through the array from the last element to the first
        for (int i = array.length - 1; i > 0; i--) {
            // Generate a random index between 0 and i (inclusive)
            int j = random.nextInt(i + 1);

            // Swap the elements at indices i and j
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }

        // Print the shuffled array
        System.out.println(Arrays.toString(array));
    }
}