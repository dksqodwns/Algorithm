import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            String cmd = st.nextToken();

            switch (cmd) {
                case "push":
                    q.offerLast(Integer.parseInt(st.nextToken()));
                    break;

                case "pop":
                    System.out.println(q.isEmpty() ? -1 : q.pollFirst());
                    break;

                case "size":
                    System.out.println(q.size());
                    break;

                case "empty":
                    System.out.println(q.isEmpty() ? 1 : 0);
                    break;

                case "front":
                    System.out.println(q.isEmpty() ? -1 : q.peekFirst());
                    break;

                case "back":
                    System.out.println(q.isEmpty() ? -1 : q.peekLast());
                    break;
            }
        }
    }
}