public class Ch1_3 {
    public static void main(String[] args) {
        String input = "Mr John Smith                  ";
        replaceSpaces(input.toCharArray(), 13);

    }

    public static void replaceSpaces(char[] str, int trueLength) {
        int spaceCount = 0;
        int index;
        int i = 0;

        for (i = 0; i < str.length; i++) {
            if (str[i] == ' ') spaceCount++;
        }

        index = trueLength + spaceCount*2;  // This is the length of the return string
        for (i = trueLength - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                 str[index-1] = '0';
                 str[index-2] = '2';
                 str[index-3] = '%';
                 index -= 3;
            } else {
                str[index-1] = str[i];
                index--;
            }
        }
    }
}
