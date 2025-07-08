import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        List<Integer> aArr = new ArrayList<>(n);
        List<Integer> bArr = new ArrayList<>(n);
        List<Integer> resultArr = new ArrayList<>();
        StringTokenizer st;
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            aArr.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++) {
            bArr.add(Integer.parseInt(st.nextToken()));
        }
        
        Collections.sort(aArr);
        bArr.sort(Collections.reverseOrder());
        long S = 0;
        
        for (int i = 0; i < n; i++) {
            S += (long)aArr.get(i) * bArr.get(i);
        }
        
        System.out.println(S);
    }
}