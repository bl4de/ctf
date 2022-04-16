import java.util.Arrays;

public class Main {

  public static char[] convert(int[] array) {
    char[] array1 = new char [100];
    int length = array.length;
    for (int i = 0; i < length; i++) {
      // this converts a integer into a character
      array1[i] = (char) array[i];
    }
    return array1;
  }

  public static void main(String[] strArr) {
    int[] iArr = new int[35];
    for (int i = 0; i < 35; i++) {
      iArr[i] = 0;
    }
    iArr[0] = 103;
    iArr[1] = iArr[0] + 2;
    iArr[2] = iArr[0];
    for (int i2 = 3; i2 < 8; i2++) {
      switch (i2) {
        case 3:
          iArr[i2] = 101;
          break;
        case 4:
          iArr[6] = 99;
          break;
        case 5:
          iArr[5] = 123;
          break;
        case 6:
          iArr[i2 + 1] = 48;
          break;
        case 7:
          iArr[4] = 109;
          break;
      }
    }
    iArr[8] = 102;
    iArr[9] = iArr[8];
    int i3 = iArr[7];
    iArr[28] = i3;
    iArr[25] = i3;
    iArr[24] = i3;
    iArr[10] = 51;
    iArr[11] = (((iArr[10] + 12) - 4) - 4) - 4;
    int pow = iArr[0] - ((int) Math.pow(2.0d, 3.0d));
    iArr[27] = pow;
    iArr[22] = pow;
    iArr[15] = pow;
    iArr[12] = pow;
    iArr[13] = 49;
    iArr[14] = 115;
    for (int i4 = 16; i4 < 22; i4++) {
      switch (i4) {
        case 16:
          iArr[i4 + 1] = 108;
          break;
        case 17:
          iArr[i4 - 1] = 52;
          break;
        case 18:
          iArr[i4 + 1] = 52;
          break;
        case 19:
          iArr[i4 - 1] = 119;
          break;
        case 20:
          iArr[i4 + 1] = 115;
          break;
        case 21:
          iArr[i4 - 1] = 121;
          break;
      }
    }
    iArr[23] = 103;
    iArr[26] = iArr[23] - 3;
    iArr[29] = iArr[26] + 20;
    iArr[30] = (iArr[29] % 53) + 53;
    iArr[31] = iArr[0] - 18;
    iArr[32] = 80;
    iArr[33] = 83;
    iArr[35 - 1] = (int) Math.pow(5.0d, 3.0d);
    System.out.println(convert(iArr));
  }
}
