// import java.util.Arrays;
// import java.util.Collections;
// import java.util.List;

// public class ShuffleArray {
//     public static void main(String[] args) {
//         Integer[] array = { 1, 2, 3, 4, 5 };

//         // Convert array to List
//         List<Integer> list = Arrays.asList(array);

//         // Shuffle the List
//         Collections.shuffle(list);
//         System.out.println(list);

//         // Convert List back to array
//         list.toArray(array);

//         // Print the shuffled array
//         System.out.println(Arrays.toString(array));
//     }
// }

import java.util.Arrays;
import java.util.Random;

public class ShuffleArray {
    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4, 5 };

        Random random = new Random();

        for (int i = array.length - 1; i > 0; i--) {
            int j = random.nextInt(i + 1);

            // Swap elements at indices i and j
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }

        // Print the shuffled array
        System.out.println(Arrays.toString(array));
    }
}