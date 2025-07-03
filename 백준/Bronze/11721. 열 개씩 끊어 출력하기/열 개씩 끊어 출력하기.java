import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < str.length(); i = i + 10) {
            String substring;
            if (i + 10 > str.length()) {
                substring = str.substring(i);
            } else {
                substring = str.substring(i, i + 10);
            }
            sb.append(substring).append("\n");
        }
        
        System.out.print(sb);
    }
}