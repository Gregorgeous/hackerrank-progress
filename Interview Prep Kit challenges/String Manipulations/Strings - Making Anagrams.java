import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    public static int numberNeeded(String first, String second) {
        int masterCounter = 0;
        StringBuilder SBFirst = new StringBuilder(first);
        StringBuilder SBSecond = new StringBuilder(second);
        int[] charTable1 = new int[26];
        int[] charTable2 = new int[26];
        int index = 0;
        int letterIndex = 0;
        while (index < first.length() && index < second.length()){
            letterIndex =  first.charAt(index) - 'a';
            charTable1[letterIndex]++;
            letterIndex =  second.charAt(index) - 'a';
            charTable2[letterIndex]++;
            index++;
        }
        int smallerWordLength = index+1;

        if (index >= first.length()) {
            while (index < second.length()){
                letterIndex =  second.charAt(index) - 'a';
                charTable2[letterIndex]++;
                index++;
            }
        } else {
            while (index < first.length()){
                letterIndex =  first.charAt(index) - 'a';
                charTable1[letterIndex]++;
                index++;
            }
        }
        int biggerWordLength = index+1;

        index = 0 ;
        while (index < charTable1.length){
            while (charTable1[index] != charTable2[index]){
                if (charTable1[index] > charTable2[index]){
                    charTable1[index]--;
                } else {
                    charTable2[index]--;
                }
                masterCounter++;
            }
            index++;
        }

        return masterCounter;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        System.out.println(numberNeeded(a, b));
    }
}
