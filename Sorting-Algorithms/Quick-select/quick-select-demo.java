import java.util.Arrays;
import java.util.Scanner;

public class QuickselectDemo {
   private static int partition(int[] numbers, int startIndex, int endIndex) {
      // Select the middle value as the pivot.
      int midpoint = startIndex + (endIndex - startIndex) / 2;
      int pivot = numbers[midpoint];
   
      // "low" and "high" start at the ends of the array segment
      // and move towards each other.
      int low = startIndex;
      int high = endIndex;
   
      boolean done = false;
      while (!done) {
         // Increment low while numbers[low] < pivot
         while (numbers[low] < pivot) {
            low = low + 1;
         }
      
         // Decrement high while pivot < numbers[high]
         while (pivot < numbers[high]) {
            high = high - 1;
         }
      
         // If low and high have crossed each other, the loop
         // is done. If not, the elements are swapped, low is
         // incremented and high is decremented.
         if (low >= high) {
            done = true;
         }
         else {
            int temp = numbers[low];
            numbers[low] = numbers[high];
            numbers[high] = temp;
            low = low + 1;
            high = high - 1;
         }
      }

      // "high" is the last index in the left segment.
      return high;
   }
    
   private static int quickselect(int[] numbers, int startIndex, int endIndex, int k) {
      if (startIndex >= endIndex) {
         return numbers[startIndex];
      }

      int lowLastIndex = partition(numbers, startIndex, endIndex);
      if (k <= lowLastIndex) {
         return quickselect(numbers, startIndex, lowLastIndex, k);
      }
      return quickselect(numbers, lowLastIndex + 1, endIndex, k);
   }

   public static void main(String[] args) {
      int[] numbers = { 6, 2, 12, 8, 4, 3, 19, 17, 22, 41, 7, 1, 15 };
      System.out.println("Original array: " + Arrays.toString(numbers));

      // Get k from user
      Scanner scnr = new Scanner(System.in);
      int k = scnr.nextInt();
      int kthValue = quickselect(numbers, 0, numbers.length - 1, k);

      // Display results, and compare to sorted list.
      System.out.printf("After quickselect(%d): %s%n", k, Arrays.toString(numbers));
      System.out.printf("quickselect(%d) result: %d%n", k, kthValue);
    
      System.out.println();
      Arrays.sort(numbers);
      System.out.println("Sorted list: " + Arrays.toString(numbers));
      System.out.printf("kth sorted item: %d%n", numbers[k]);
   }
}

// output
// Original array: [6, 2, 12, 8, 4, 3, 19, 17, 22, 41, 7, 1, 15]
// After quickselect(5): [1, 2, 3, 4, 6, 7, 8, 12, 17, 15, 41, 22, 19]
// quickselect(5) result: 7

// Sorted list: [1, 2, 3, 4, 6, 7, 8, 12, 15, 17, 19, 22, 41]
// kth sorted item: 7