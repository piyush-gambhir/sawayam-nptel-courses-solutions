import java.util.Scanner;

public class Solution {

    private static long dfs(int n, int m, long[][] a, int i, int j) {
        if (i < 0 || j < 0)
            return 0;
        if (i >= n || j >= m)
            return 0;
        if (a[i][j] == 0)
            return 0;

        long k = a[i][j];
        a[i][j] = 0;
        return k + dfs(n, m, a, i + 1, j) + dfs(n, m, a, i, j + 1) + dfs(n, m, a, i - 1, j) + dfs(n, m, a, i, j - 1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        long ans = 0;
        long[][] a = new long[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = scanner.nextLong();
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] != 0) {
                    long sum = dfs(n, m, a, i, j);
                    ans = Math.max(sum, ans);
                }
            }
        }

        System.out.print(ans);
    }
}
