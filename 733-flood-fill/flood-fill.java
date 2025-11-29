class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original_color = image[sr][sc];

        if (image[sr][sc] == color) return image;

        fill(image, sr, sc, color, original_color);

        return image;

    }

    private void fill(int[][] image, int sr, int sc, int color, int original_color) {
        int m = image.length;
        int n = image[0].length;

        if (sr < 0 || sr >= m || sc < 0 || sc >= n || image[sr][sc] != original_color) {
            return;
        }

        image[sr][sc] = color;

        fill(image, sr - 1, sc, color, original_color);
        fill(image, sr + 1, sc, color, original_color);
        fill(image, sr, sc - 1, color, original_color);
        fill(image, sr, sc + 1, color, original_color);


    }

}