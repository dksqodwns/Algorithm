import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> time_list = new ArrayList<>();
        ArrayList<Integer> step_list = new ArrayList<>();

        int sum = 0;
        int result = 0;
        int N = Integer.parseInt(br.readLine());
        String[] input_list = br.readLine().split(" ");

        for (String time : input_list) {
            time_list.add(Integer.parseInt(time));
        }

        time_list.sort(Integer::compareTo);

        for (int i = 0; i < N; i++) {
            sum += time_list.get(i);
            step_list.add(sum);
        }

        for (int step : step_list) {
            result += step;
        }

        System.out.println(result);
    }
}