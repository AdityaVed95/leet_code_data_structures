class Solution {
    public static boolean containsDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            System.out.println(i);
        }

        return true;
    }

    public static void main(String[] args) {
        int nums[] = {1, 2, 3, 4, 5, 6};
        boolean ans = containsDuplicate(nums);
        System.out.println(ans);

    }
}