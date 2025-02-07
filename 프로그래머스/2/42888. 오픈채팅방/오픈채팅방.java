import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {

    public static final String ENTER = "Enter";
    public static final String LEAVE = "Leave";
    public static final String CHANGE = "Change";
    
    
    public String[] solution(String[] record) {
        // 유저를 저장 해둘 해시맵
        HashMap<String, String> userMap = new HashMap<>();
        // answer 로그를 저장 해둘 리스트
        List<String[]> logs = new ArrayList<>();

        for (String entry : record) {
            String[] tokens = entry.split(" ");
            String action = tokens[0];
            String userId = tokens[1];

            if (action.equals(ENTER)) {
                String nickName = tokens[2];
                // 유저 입장
                userMap.put(userId, nickName);
                // 로그 저장
                logs.add(new String[]{userId, ENTER});
            } else if (action.equals(LEAVE)) {
                // 로그만 저장
                logs.add(new String[]{userId, LEAVE});
            } else if (action.equals(CHANGE)) {
                String nickName = tokens[2];
                // 유저 변경
                userMap.put(userId, nickName);
            }
        }
        
        // 로그 사이즈만큼 answer 배열 생성
        String[] answer = new String[logs.size()];
        int index = 0;
        
        for (String[] log : logs) {
            String userId = log[0];
            String action = log[1];
            String nickName = userMap.get(userId);

            if (action.equals(ENTER)) {
                answer[index++] = nickName + "님이 들어왔습니다.";
            } else if (action.equals(LEAVE)) {
                answer[index++] = nickName + "님이 나갔습니다.";
            }
        }

        return answer;
    }
}