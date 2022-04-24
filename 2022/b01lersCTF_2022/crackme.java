import java.util.Random;
import java.util.Scanner;

public class CrackMe {

  public static void main(String[] paramArrayOfString) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("What is the flag?");
    String str1 = scanner.nextLine();
    if (str1.length() != 22) {
      System.out.println("Not the flag :(");
      return;
    }
    char[] arrayOfChar = new char[str1.length()];
    int i;
    for (i = 0; i < str1.length(); i++) {
      arrayOfChar[i] = str1.charAt(i);
    }
    for (i = 0; i < str1.length() / 2; i++) {
      char c = arrayOfChar[str1.length() - i - 1];
      arrayOfChar[str1.length() - i - 1] = arrayOfChar[i];
      arrayOfChar[i] = c;
    }
    int[] arrayOfInt1 = {
      19,
      17,
      15,
      6,
      9,
      4,
      18,
      8,
      16,
      13,
      21,
      11,
      7,
      0,
      12,
      3,
      5,
      2,
      20,
      14,
      10,
      1,
    };
    int[] arrayOfInt2 = new int[arrayOfChar.length];
    for (int j = arrayOfInt1.length - 1; j >= 0; j--) {
      arrayOfInt2[j] = arrayOfChar[arrayOfInt1[j]];
    }

    Random random = new Random();
    random.setSeed(431289L);
    int[] arrayOfInt3 = new int[str1.length()];
    for (byte b1 = 0; b1 < str1.length(); b1++) {
      arrayOfInt3[b1] = arrayOfInt2[b1] ^ random.nextInt(b1 + true);
    }

    String str2 = "";
    for (byte b2 = 0; b2 < arrayOfInt3.length; b2++) {
      str2 = str2 + str2 + ".";
    }
    System.out.println("\nYOUR FLAG: " + str2);
    if (
      str2.equals(
        "116.122.54.50.93.66.98.117.75.51.97.78.104.119.90.53.94.36.105.84.40.69."
      )
    ) {
      System.out.println("Congrats! You got the flag!");
    } else {
      System.out.println("Not the flag :(");
    }
  }
}
