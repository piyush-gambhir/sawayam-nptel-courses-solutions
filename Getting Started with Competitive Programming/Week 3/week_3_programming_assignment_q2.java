import java.util.*;
import java.io.*;

public class OptimalSchedule {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int m = Integer.parseInt(input[0]);
        int n = Integer.parseInt(input[1]);
        int d = Integer.parseInt(input[2]);

        String[] maverickAvailabilities = br.readLine().split(" ");
        String[] gooseAvailabilities = br.readLine().split(" ");

        List<Pair> combinedAvailabilities = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            combinedAvailabilities.add(new Pair(Integer.parseInt(maverickAvailabilities[i]), i));
        }
        for (int i = 0; i < n; i++) {
            combinedAvailabilities.add(new Pair(Integer.parseInt(gooseAvailabilities[i]), m + i));
        }

        Collections.sort(combinedAvailabilities, Collections.reverseOrder());

        List<Pair> selectedAvailabilities = new ArrayList<>();

        for (int i = 0; i < d; i++) {
            selectedAvailabilities.add(combinedAvailabilities.get(i));
        }

        Collections.sort(selectedAvailabilities, (a, b) -> a.index - b.index);

        for (Pair pair : selectedAvailabilities) {
            System.out.print(pair.value + " ");
        }
    }
}

class Pair implements Comparable<Pair> {
    int value;
    int index;

    Pair(int value, int index) {
        this.value = value;
        this.index = index;
    }

    @Override
    public int compareTo(Pair other) {
        return Integer.compare(this.value, other.value);
    }
}
