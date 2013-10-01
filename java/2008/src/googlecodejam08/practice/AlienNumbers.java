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
 * @author Diogo Luiz Böhm
 */
public class AlienNumbers {
    TextScanner textFile;
    Vector<String> cases;
    int caseCount;
    
    
    public AlienNumbers(String string) throws FileNotFoundException {
        textFile = new TextScanner(string);
        caseCount = Integer.parseInt(textFile.getCurLine());
        cases = new Vector<String>();
        for(int x=0;x<caseCount;x++){
            this.solveCase(x+1);
            this.printCase(x);
        }
    }
    
    private void solveCase(int curCase){
        textFile.advanceLine();
        String[] fields = textFile.getCurLine().split(" ");
        
        String number = fields[0],system = fields[1], target=fields[2];
        Vector<String> temp = new Vector<String>(),thisCase = new Vector<String>();
        
        int tempCount=0,thisCount=0,aux;
        
        temp.add(""+system.charAt(0));
        thisCase.add(""+target.charAt(0));
        
        String cmp="",cmp2="";
        
        while (!cmp.equals(number)){
            if (tempCount==system.length()){
                
                int y=0;
                temp.setElementAt(""+system.charAt(0), y);
                for (y=1;y<temp.size();y++){
                    if (temp.get(y).equals(""+system.charAt(system.length()-1))){
                        temp.setElementAt(""+system.charAt(0), y);
                    } else {
                        temp.setElementAt(""+system.charAt(system.lastIndexOf(temp.get(y))+1), y);
                        break;
                    }
                }
                if (temp.get(temp.size()-1).equals(""+system.charAt(0)))
                    temp.add(""+system.charAt(1));
                tempCount=1;
            } else {
                temp.setElementAt(""+system.charAt(tempCount),0);
                tempCount++;
            }
            
            
            
            if (thisCount==target.length()){
                
                int y=0;
                thisCase.setElementAt(""+target.charAt(0), y);
                for (y=1;y<thisCase.size();y++){
                    if (thisCase.get(y).equals(""+target.charAt(target.length()-1))){
                        thisCase.setElementAt(""+target.charAt(0), y);
                    } else {
                        thisCase.setElementAt(""+target.charAt(target.lastIndexOf(thisCase.get(y))+1), y);
                        break;
                    }
                }
                if (thisCase.get(thisCase.size()-1).equals(""+target.charAt(0)))
                    thisCase.add(""+target.charAt(1));
                thisCount=1;
            } else {
                thisCase.setElementAt(""+target.charAt(thisCount),0);
                thisCount++;
            }
            
            
            
            cmp = "";
            for (int x=temp.size()-1;x>=0;x--){
                cmp=cmp+(temp.get(x));
            }
            
            cmp2 = "";
            for (int x=thisCase.size()-1;x>=0;x--){
                cmp2=cmp2+(thisCase.get(x));
            }
        
            //System.out.println(cmp+" "+number+" "+cmp2);
        }
        
        String ret = "";
        for (int x=thisCase.size()-1;x>=0;x--){
            ret=ret+(thisCase.get(x));
        }
        cases.add(ret);
    }
    private void printCase(int curCase){
        System.out.println("Case #"+(curCase+1)+": "+cases.get(curCase));
    }
}
