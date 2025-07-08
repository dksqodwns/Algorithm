import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        HashSet<Integer> nSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            nSet.add(Integer.parseInt(st.nextToken()));
        }
        
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            sb.append(nSet.contains(target) ? "1 " : "0 ");
        }
        
        if (sb.length() > 0) {
            sb.setLength(sb.length() - 1);
        }
        
        System.out.println(sb);
    }
}