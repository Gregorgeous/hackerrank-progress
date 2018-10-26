import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    int [] arr;
    int numOfShifts;
    Solution (int[] _arr , int _numOfShifts ){
        this.arr = _arr;
        numOfShifts = _numOfShifts % arr.length;
        for (int i = 0; i < numOfShifts; i++) {
            shiftByOne();
        }
        for (int elem:arr) {
            System.out.print(elem + " ");
        }
    }

    public void shiftByOne (){
        int [] newArray = arr;
        int temp = newArray[0];
        for (int i = 0; i < newArray.length-1; i++) {
            newArray[i] = newArray[i+1];
        }
        newArray[newArray.length-1] = temp;
        arr = newArray;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        Solution s = new Solution(a, k );
    }
}