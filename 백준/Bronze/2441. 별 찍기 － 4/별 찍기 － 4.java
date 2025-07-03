import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i <= n; i++) {
            int emptySpace = i;
            int starSpace = n - emptySpace;

            for (int j = 1; j <= emptySpace; j++) {
                System.out.print(" ");
            }

            for (int k = 1; k <= starSpace; k++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}