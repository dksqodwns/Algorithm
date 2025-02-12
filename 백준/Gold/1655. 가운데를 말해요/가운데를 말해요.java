import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> lowers = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> highers = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());

            if (lowers.isEmpty() || num <= lowers.peek()) {
                lowers.offer(num);
            } else {
                highers.offer(num);
            }

            if (lowers.size() - highers.size() > 1) {
                highers.offer(lowers.poll());
            } else if (highers.size() - lowers.size() > 0) {
                lowers.offer(highers.poll());
            }

            sb.append(lowers.peek()).append("\n");
        }

        System.out.println(sb);
    }
}