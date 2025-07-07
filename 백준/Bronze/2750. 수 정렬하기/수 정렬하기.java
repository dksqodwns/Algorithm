import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> aArr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            aArr.add(Integer.parseInt(br.readLine()));
        }
        aArr.sort(Integer::compareTo);
        for (int x: aArr) {
            System.out.println(x);
        }
    }
}