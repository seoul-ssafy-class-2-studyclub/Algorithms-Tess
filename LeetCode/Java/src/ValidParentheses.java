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
//
//
//class Solution {
//
//    // Hash table that takes care of the mappings.
//    // Character이라는 객체로 추가해준다.
//    private HashMap<Character, Character> mappings;
//
//    // Initialize hash map with mappings. This simply makes the code easier to read.
//    public Solution() {
//        this.mappings = new HashMap<Character, Character>();
//        this.mappings.put(')', '(');
//        this.mappings.put('}', '{');
//        this.mappings.put(']', '[');
//    }
//
//    public boolean isValid(String s) {
//
//        // Initialize a stack to be used in the algorithm.
//        Stack<Character> stack = new Stack<Character>();
//
//        for (int i = 0; i < s.length(); i++) {
//            char c = s.charAt(i);
//
//            // If the current character is a closing bracket.
//            if (this.mappings.containsKey(c)) {
//
//                // Get the top element of the stack. If the stack is empty, set a dummy value of '#'
//                char topElement = stack.empty() ? '#' : stack.pop();
//
//                // If the mapping for this bracket doesn't match the stack's top element, return false.
//                if (topElement != this.mappings.get(c)) {
//                    return false;
//                }
//            } else {
//                // If it was an opening bracket, push to the stack.
//                stack.push(c);
//            }
//        }
//
//        // If the stack still contains elements, then it is an invalid expression.
//        return stack.isEmpty();
//    }
//}
