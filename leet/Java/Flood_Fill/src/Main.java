import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution test = new Solution();

        int[][] image = {{1,1,1},{1,1,0},{1,0,1}};
        int sr = 1; int sc = 1; int newColor = 2;

        int[][] check = test.floodFill(image, sr, sc, newColor);

        System.out.println(Arrays.deepToString(check));
    }
}
