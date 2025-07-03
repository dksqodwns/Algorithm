import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        for (int i = 1; i <= n; i++) {
            int emptySpace = n - i;
            int starSpace = i;
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