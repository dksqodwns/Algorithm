import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ArrayDeque<Integer> q = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            String cmd = st.nextToken();

            switch (cmd) {
                case "push": {
                    q.offerFirst(Integer.parseInt(st.nextToken()));
                    break;
                }
                case "pop": {
                    if (q.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(q.pollFirst());
                    }
                    break;
                }
                case "top": {
                    if (q.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(q.peekFirst());
                    }
                    break;
                }
                case "size":
                    System.out.println(q.size());
                    break;
                case "empty": {
                    if (q.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                }
            }
        }
    }
}