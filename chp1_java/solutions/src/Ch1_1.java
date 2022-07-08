import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Ch1_1 {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        System.out.println(containsDuplicate(nums));

        String test = "eagle";
        String test2 = "abcdefghi";

        System.out.println(isUnique3(test));
        System.out.println(isUnique3(test2));
    }

    // Leetcode version: https://leetcode.com/problems/contains-duplicate/
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int x : nums) {
            if (set.contains(x)) return true;
            set.add(x);
        }
        return false;
    }

    // From the book
    public static boolean isUnique(String s) {
        Set<Character> set = new HashSet<>(s.length());

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (set.contains(c)) return false;
            set.add(c);
        }
        return true;
    }

    public static boolean isUnique2(String s) {
        if (s.length() > 128) return false;  // Assuming ASCII (non-extended)

        boolean[] char_set = new boolean[128];
        for (int i = 0; i < s.length(); i++) {
            int val = s.charAt(i);  // Note we cast the char to an int so we can index into the array.
            if (char_set[val]) return false;
            char_set[val] = true;
        }
        return true;
    }

    public static boolean isUnique3(String s) {
        int checker = 0;

        for (int i = 0; i < s.length(); i++) {
            int val = s.charAt(i) - 'a';  // Get integer representation between 0-25
            if ( (checker & (1 << val)) > 0 ) {
                return false;
            }
            checker |= (1 << val);
        }

        return true;
    }




}
