import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Deque<Character> left = new ArrayDeque<>(), right = new ArrayDeque<>();
        for (char c : br.readLine().toCharArray()) {
            left.push(c);
        }

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            String cmd = st.nextToken();
            switch (cmd) {
                case "L":
                    if (!left.isEmpty()) {
                        right.push(left.pop());
                    }
                    break;
                case "D":
                    if (!right.isEmpty()) {
                        left.push(right.pop());
                    }
                    break;
                case "B":
                    if (!left.isEmpty()) {
                        left.pop();
                    }
                    break;
                case "P":
                    left.push(st.nextToken().charAt(0));
                    break;
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!left.isEmpty()) {
            sb.append(left.removeLast());
        }
        while (!right.isEmpty()) {
            sb.append(right.pop());
        }

        System.out.println(sb);

    }
}