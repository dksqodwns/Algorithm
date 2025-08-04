import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int start = Integer.parseInt(input[0]);
        int end = Integer.parseInt(input[1]);

        boolean[] isNotPrime = new boolean[end + 1];
        isNotPrime[0] = true;
        isNotPrime[1] = true;

        for (int i = 2; i * i <= end; i++) {
            if (!isNotPrime[i]) {
                for (int j = i * i; j <= end; j += i) {
                    isNotPrime[j] = true;
                }
            }
        }

        for (int i = start; i <= end; i++) {
            if (!isNotPrime[i]) {
                bw.write(i + "\n");
            }
        }

        bw.flush();
        bw.close();
    }
}
