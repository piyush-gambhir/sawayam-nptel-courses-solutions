import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] granites = new int[n];

        for (int i = 0; i < n; i++) {
            granites[i] = sc.nextInt();
        }

        List<Stack<Integer>> gopurams = new ArrayList<>();

        for (int granite : granites) {
            boolean placed = false;
            for (Stack<Integer> gopuram : gopurams) {
                if (gopuram.peek() > granite) {
                    gopuram.push(granite);
                    placed = true;
                    break;
                }
            }
            if (!placed) {
                Stack<Integer> newGopuram = new Stack<>();
                newGopuram.push(granite);
                gopurams.add(newGopuram);
            }
        }

        System.out.print(gopurams.size());
    }
}
