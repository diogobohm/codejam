/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package googlecodejam08;

import java.io.FileNotFoundException;
import java.util.Vector;
/**
 *
 * @author diogo
 */
public class SavingTheUniverse {
    TextScanner textFile;
    Vector<String> cases;
    int caseCount;
    
    
    public SavingTheUniverse(String string) throws FileNotFoundException {
        textFile = new TextScanner(string);
        caseCount = Integer.parseInt(textFile.getCurLine());
        cases = new Vector<String>();
        for(int x=0;x<caseCount;x++){
            this.solveCase(x+1);
            this.printCase(x);
        }
    }
    
    private void solveCase(int curCase){
        
        //initializes the case vars
        Vector<String> searchEngines;
        String[] queries;
        int[] counter,range;
        
        textFile.advanceLine();
        int x,limit = Integer.parseInt(textFile.getCurLine());
        searchEngines = new Vector<String>();
        counter = new int[limit];
        range = new int[limit];
        
        for (x=0;x<limit;x++){
            textFile.advanceLine();
            searchEngines.add(textFile.getCurLine());
        }
        
        textFile.advanceLine();
        limit = Integer.parseInt(textFile.getCurLine());
        queries = new String[limit];
        for (x=0;x<limit;x++){
            textFile.advanceLine();
            queries[x] = textFile.getCurLine();
        }
        
        int hits=0;
        boolean done = false;
        int startingPoint=0;//,lessSearched=-1;
        int last=-1, bigger;
        int y=0;
        String result="";
        //solves
        while(!done){
            
            for (x=0;x<counter.length;x++){
                if (x==last){
                    range[x]=0;
                } else{
                    range[x]=-1;
                }
            }
            
            for (y=0;y<range.length;y++)
                for (x=startingPoint;x<queries.length;x++){
                    if (searchEngines.indexOf(queries[x])==y && range[y]==-1){
                        range[y]=x-startingPoint;
                        break;
                    }
                }
            
            last=-1;
            bigger=-1;
            for (x=0;x<range.length;x++){
                if (range[x]==-1)
                    done= true;
                else if(range[x]>bigger){
                    bigger = range[x];
                    last=x;
                }
            }
            
            if (!done){
                for (x=startingPoint;x<queries.length;x++){
                    if(queries[x].equals(searchEngines.get(last))){
                        startingPoint=x;
                        break;
                    }
                }
            
                hits++;
                result=result+" "+searchEngines.get(last)+",";
            }
        }
        
        //adds solution
        cases.add(String.valueOf(hits));//+" "+result);
    }
    private void printCase(int curCase){
        System.out.println("Case #"+(curCase+1)+": "+cases.get(curCase));
    }
}
