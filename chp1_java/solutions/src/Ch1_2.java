public class Ch1_2 {
    public static void main(String[] args) {
        String s1 = "abcd";
        String t1 = "bcad";

        String s2 = "poop";
        String t2 = "foop";

        System.out.println(checkPermutation(s1, t1));
        System.out.println(checkPermutation(s2, t2));


    }

    public static boolean checkPermutation(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] letters = new int[128];  // Assume non-extended ASCII

        char[] s_array = s.toCharArray();
        for (char c: s_array) {
            letters[c]++;
        }

        char[] t_array = t.toCharArray();
        for (char c: t_array) {
            letters[c]--;
            if (letters[c] < 0) return false;
        }
        return true;
    }

    // Less efficient (time) sorting solution
    public static String sort(String s) {
        char[] content = s.toCharArray();
        java.util.Arrays.sort(content);
        return new String(content);
    }

    public static boolean checkPermutation2(String s, String t) {
        if (s.length() != t.length()) return false;
        return sort(s).equals(sort(t));
    }


}
