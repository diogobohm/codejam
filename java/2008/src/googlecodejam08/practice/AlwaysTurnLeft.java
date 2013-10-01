/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package googlecodejam08.practice;

import googlecodejam08.*;
import java.io.FileNotFoundException;
import java.util.Vector;

/**
 *
 * @author diogo
 */
public class AlwaysTurnLeft {
    TextScanner textFile;
    Vector<String>[] cases;
    
    public AlwaysTurnLeft(String string) throws FileNotFoundException {
        textFile = new TextScanner(string);
        int caseCount = Integer.parseInt(textFile.getCurLine());
        for(int x=0;x<caseCount;x++){
            this.solveCase(x+1);
            this.printCase(x);
        }
    }
    
    int curDir;
    private void solveCase(int curCase){
        String en2ex = textFile.getCurLine().split(" ")[0], ex2en = textFile.getCurLine().split(" ")[1];
        cases[curCase-1] = new Vector<String>();
        int curRow=0,curCol=0;
        curDir=2;
        String now="";
        for (int x=0;x<en2ex.length();x++){
            if (x==0){
                curRow=0;curCol=0;
                now = "1";
            } else{
                if(en2ex.charAt(x)=='W'){
                    if (curDir==0){
                        cases[curCase-1].add(now);
                        curRow--;
                    }else if (curDir==2){
                        cases[curCase-1].add(now);
                        curRow++;
                        now="1";
                    }else if (curDir==1){
                        
                    }
                } else if(en2ex.charAt(x)=='R'){
                    this.turn(false);
                } else if(en2ex.charAt(x)=='L'){
                    this.turn(true);
                }
            }
        }
        //north 1, south 2, west 4, east 8
    }
    
    private void turn(boolean left){
        if (left){
            if (curDir==0)
                curDir=4;
            else
                curDir--;
        }else{
            if (curDir==4)
                curDir=0;
            else
                curDir++;
        }
    }
    
    private void printCase(int curCase){
        System.out.println("Case #"+(curCase+1));
        for (int x=0;x<cases[curCase].size();x++){
            System.out.println(cases[curCase].get(x));
        }
    }
}
