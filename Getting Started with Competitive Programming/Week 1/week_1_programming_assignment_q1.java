import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            long[] vk = new long[n];
            long[] lm = new long[m];
            for (int i = 0; i < n; i++) {
                vk[i] = scanner.nextLong();
            }
            for (int i = 0; i < m; i++) {
                lm[i] = scanner.nextLong();
            }
            int i = 0, j = 0;
            while (i < n && j < m) {
                if (vk[i] == lm[j]) {
                    vk[i] = 0;
                    lm[j] = 0;
                    i++;
                    j++;
                } else if (vk[i] > lm[j]) {
                    vk[i] -= lm[j];
                    j++;
                } else {
                    lm[j] -= vk[i];
                    i++;
                }
            }
            if (i == n && j == m) {
                System.out.println("Draw");
            } else if (i == n) {
                long cost = 0;
                for (int k = j; k < m; k++) {
                    cost += lm[k];
                    if (cost > 0) {
                        break;
                    }
                }
                if (cost > 0) {
                    System.out.println("Duryodhana");
                } else {
                    System.out.println("Draw");
                }
            } else {
                long cost = 0;
                for (int k = i; k < n; k++) {
                    cost += vk[k];
                    if (cost > 0) {
                        break;
                    }
                }
                if (cost > 0) {
                    System.out.println("Yudhisthira");
                } else {
                    System.out.println("Draw");
                }
            }
        }
        scanner.close();
    }
}
