import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();
        HashMap<String, String> mapping = new HashMap<>();
        mapping.put(")", "(");
        mapping.put("}", "{");
        mapping.put("]", "[");
        for (int i = 0; i < s.length() ;i++) {

            // 문자열에서 한 글자만 가져오기 위해서는 다음과 같은 메소드를 사용
            // charAt()
            char charL = s.charAt(i);
            String CheckL = Character.toString(charL);
            if (mapping.containsKey(CheckL)) {
                if(stack.size() == 0) {
                    String topElement;
                    topElement = "#";
                    if (mapping.get(CheckL) != topElement) {
                        return false;
                    }
                } else {
                    String topElement = stack.pop();
                }

            } else {
                stack.push(CheckL);
            }
        }
        return stack.empty();
    }
}
