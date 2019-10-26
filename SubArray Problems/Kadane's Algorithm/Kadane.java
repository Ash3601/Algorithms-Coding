import java.util.*;

class Kadane {

    public static int kadanesAlgorithm(int[] array) {
        // # check the first with the addition and check if the current sum
        // # is greater than the number itself
        // # after that we check it with the array that keeps track of the max element
        List<Integer> currentSum = new ArrayList<>();
        currentSum.add(array[0]);
        List<Integer> maxSumSoFar = new ArrayList<>();
        System.out.println("Hello");
        return 19;
    }

    public static void main(String args[]) {
        int[] array = { 3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4 };
        kadanesAlgorithm(array);
    }
}