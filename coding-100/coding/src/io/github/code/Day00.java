package io.github.code;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * 【顺时针螺旋矩阵】 给定一个包含 m x n 个元素的矩阵（m 行 n 列） 按照顺时针螺旋顺序，返回矩阵中的所有元素
 * 【示例输入：】
 *  [ [1,2,3], [4,5,6], [7,8,9] ]
 * 【示例输出：】
 *  [1,2,3,6,9,8,7,4,5]
 */
public class Day00 {
    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int height = matrix.length;
        int width = height == 0 ? 0 : matrix[0].length;
        int size = height * width;

        int[] dirX = {0, 1, 0, -1};
        int[] dirY = {1, 0, -1, 0};

        // 初始化起点坐标：(0,-1)方向：向右
        int x = 0;
        int y = -1;
        int dir = 0;

        for (int step = 0, total = 0; total < size; total += step) {
            // 根据方向得到对应的位移，并修正此后矩阵的参数（此后线段的长度）
            if (dir == 0 || dir == 2) {
                step = width;
                height--;
            } else {
                step = height;
                width--;
            }
            // 此前确定了起点坐标、方向和位移，就可以得到当前线段所有坐标，并输出到结果集：
            for (int i = step; i > 0; i--) {
                x += dirX[dir];
                y += dirY[dir];
                result.add(matrix[x][y]);
            }
            // 调整下一条线段的方向
            dir = ++dir % 4;
        }
        return result;
    }

    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
        List<Integer> result = spiralOrder(matrix);
        Iterator<Integer> iterator = null;
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append('[');
//        for (iterator = result.iterator(); iterator.hasNext(); ) {
//            stringBuilder.append(iterator.next().toString() + ',');
//        }

        for (int i=0;i<result.size();i++){
            stringBuilder.append(result.get(i).toString()+ ",");
        }
        stringBuilder.append(']');
        System.out.println(stringBuilder);

    }
}