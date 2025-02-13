import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int R, C;
    static char[][] lake;

    static boolean[][] waterVisited; // 물/빙판 방문 체크 (빙판이 물로 바뀌는 과정)
    static boolean[][] swanVisited;  // 백조 이동 방문 체크

    // 현재(오늘) 물 칸들의 가장자리 빙판
    static Queue<int[]> waterQ = new LinkedList<>();
    // 내일 녹일 빙판
    static Queue<int[]> waterQNext = new LinkedList<>();

    // 오늘 백조가 이동할 수 있는 물 칸
    static Queue<int[]> swanQ = new LinkedList<>();
    // 내일(빙판 녹은 뒤) 이동 가능해질 칸
    static Queue<int[]> swanQNext = new LinkedList<>();

    // 방향
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    // 백조 위치
    static int swan1x, swan1y;
    static int swan2x, swan2y;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] rc = br.readLine().split(" ");
        R = Integer.parseInt(rc[0]);
        C = Integer.parseInt(rc[1]);

        lake = new char[R][C];
        waterVisited = new boolean[R][C];
        swanVisited = new boolean[R][C];

        int swanCount = 0;

        // 입력 받기
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                lake[i][j] = line.charAt(j);
                if (lake[i][j] == 'L') {
                    // 백조 위치 저장
                    if (swanCount == 0) {
                        swan1x = i;
                        swan1y = j;
                        swanCount++;
                    } else {
                        swan2x = i;
                        swan2y = j;
                    }
                }
            }
        }

        // 1) 지도 전체를 돌며, '물'이거나 'L'이면 waterQ에 전부 넣는다.
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if ((lake[i][j] == '.' || lake[i][j] == 'L') && !waterVisited[i][j]) {
                    waterVisited[i][j] = true;
                    waterQ.offer(new int[]{i, j});
                }
            }
        }

        // 2) 백조1 위치 swanQ에 넣고 방문 체크
        swanVisited[swan1x][swan1y] = true;
        swanQ.offer(new int[]{swan1x, swan1y});

        int days = 0;

        // 매일 반복
        while (true) {
            // 1) 백조 이동 -> 만나면 종료
            if (moveSwan()) {
                System.out.println(days);
                return;
            }
            // 2) 못 만났으면 빙판 녹이기
            meltIce();
            days++;
        }
    }

    // 백조 이동 BFS: 오늘 이미 '물'인 칸으로만 이동
    // 아직 'X'인 칸은 내일 이동 가능(swanQNext에)
    private static boolean moveSwan() {
        while (!swanQ.isEmpty()) {
            int[] cur = swanQ.poll();
            int x = cur[0], y = cur[1];

            // 다른 백조 위치에 도달했으면 만난 것
            if (x == swan2x && y == swan2y) {
                return true;
            }

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                    continue;
                }
                if (swanVisited[nx][ny]) {
                    continue;
                }

                swanVisited[nx][ny] = true;

                if (lake[nx][ny] == '.' || lake[nx][ny] == 'L') {
                    // 오늘 이동 가능
                    swanQ.offer(new int[]{nx, ny});
                } else if (lake[nx][ny] == 'X') {
                    // 빙판이면 내일 이동
                    swanQNext.offer(new int[]{nx, ny});
                }
            }
        }
        return false;
    }

    // 빙판 녹이기
    // waterQ에는 "이미 물이라고 판정된 칸"이 들어있고,
    // 그 물 칸 주변의 빙판을 찾아서 waterQNext에 넣는다.
    private static void meltIce() {
        while (!waterQ.isEmpty()) {
            int[] cur = waterQ.poll();
            int x = cur[0], y = cur[1];

            // 이 칸이 물이니까, 인접 칸이 빙판이면 녹임
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                    continue;
                }

                if (!waterVisited[nx][ny]) {
                    waterVisited[nx][ny] = true;

                    if (lake[nx][ny] == 'X') {
                        // 빙판을 녹여 -> 내일이 아니라 "바로" 물로 만든다
                        lake[nx][ny] = '.';
                        waterQNext.offer(new int[]{nx, ny});
                    } else {
                        // 이미 물이면 계속 확장
                        waterQ.offer(new int[]{nx, ny});
                    }
                }
            }
        }

        // waterQNext에 녹은 칸들이 들어있음 -> 전부 물칸이 되었으니 waterQ로 옮김
        while (!waterQNext.isEmpty()) {
            waterQ.offer(waterQNext.poll());
        }

        // swanQNext(내일 갈 수 있었던 빙판들) 오늘 갈 수 있는 '물'이 됨
        while (!swanQNext.isEmpty()) {
            swanQ.offer(swanQNext.poll());
        }
    }
}