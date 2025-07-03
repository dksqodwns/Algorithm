import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        for (int i = n; i >= 1; i--) {
            int starSpace = i;
            
            for (int j = 0; j < starSpace; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}