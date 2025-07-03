import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int index = 0;
        int[] intArr = new int[n];

        while (st.hasMoreTokens()) {
            intArr[index] = Integer.parseInt(st.nextToken());
            index++;
        }

        Arrays.sort(intArr);
        System.out.println(intArr[0] + " " + intArr[n - 1]);
    }
}