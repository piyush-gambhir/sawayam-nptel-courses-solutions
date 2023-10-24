#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string text1, string text2) {
    int m = text1.size();
    int n = text2.size();
    
    // Create a 2D array dp to store the lengths of LCS.
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
s
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // dp[m][n] contains the length of LCS between text1 and text2.
    return dp[m][n];
}

int main() {
    string text1, text2;
    cin >> text1 >> text2;

    int result = longestCommonSubsequence(text1, text2);
    cout << "Length of Longest Common Subsequence: " << result << endl;

    return 0;
}
