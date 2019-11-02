package io.github.code;

import java.util.Stack;
import java.util.regex.Pattern;

/**
 * 【基本的计算器】
 * 实现一个基本的计算器来计算一个简单的字符串所表达的值
 * 字符串表达式仅包含非负整数，"+，-，*，/"四种运算符和空格
 * 整数除法仅保留整数部分
 * 【示例输入：】
 * 3 + 5 / 2
 * 【示例输出：】
 * 5
 */
public class Day01 {
    public static int calculate(String s) {
        // 有个测试用例int 型会超过范围
        long n = s.length();
        int num = 0, result = 0;
        // 假设第一个运算符为+，即第一个数直接入栈
        char op = '+';
        Stack<Integer> nums = new Stack<>();

        for (int i = 0; i < n; ++i) {
            // 是数字
            if (Character.isDigit(s.charAt(i))) {
                num = num * 10 + Integer.parseInt(String.valueOf(s.charAt(i)));
            }
            // 是运算符或最后一个数字
            if ((Character.isDigit(s.charAt(i)) && s.charAt(i)==' ') || i == n - 1) {
                if (op == '+') nums.push(num);
                if (op == '-') nums.push(-num);
                if (op == '*' || op == '/') {
                    int temp = (op == '*') ? nums.firstElement() * num : nums.firstElement() / num;
                    nums.pop();
                    nums.push(temp);
                }
                op = s.charAt(i);
                num = 0;
            }
        }
        while (!nums.isEmpty()) {
            result += nums.firstElement();
            nums.pop();
        }
        return Math.toIntExact(result);
    }

    public static boolean isNumeric(String str){
        Pattern pattern = Pattern.compile("^[-\\+]?[\\d]*$");
        boolean matches = pattern.matcher(str).matches();
        return matches;

    }

    public static void main(String[] args) {
        String s = "1+2";
        System.out.println(calculate(s));
    }
}
