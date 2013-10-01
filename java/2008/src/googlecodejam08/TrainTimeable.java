/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package googlecodejam08;

import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.List;
import java.util.Vector;
/**
 *
 * @author diogo
 */
public class TrainTimeable {
    TextScanner textFile;
    Vector<String> cases;
    int caseCount;
    
    
    public TrainTimeable(String string) throws FileNotFoundException {
        textFile = new TextScanner(string);
        caseCount = Integer.parseInt(textFile.getCurLine());
        cases = new Vector<String>();
        for(int x=0;x<caseCount;x++){
            this.solveCase(x+1);
            this.printCase(x);
        }
    }
    
    private boolean canBeTaken(String firstLine, String secondLine, int turnTime){
        String endFirstLine,initSecondLine;
        
        int mins,hours;
        endFirstLine=firstLine.split(" ")[1];
        hours = Integer.parseInt(endFirstLine.split(":")[0]);
        mins = Integer.parseInt(endFirstLine.split(":")[1]);
        
        hours += Math.round(turnTime/60);
        
        if (mins+turnTime>59){
            mins = (mins+turnTime)%60;
            hours++;
        } else {
            mins = mins+turnTime;
        }
        
        int minsB,hoursB;
        initSecondLine=secondLine.split(" ")[0];
        hoursB = Integer.parseInt(initSecondLine.split(":")[0]);
        minsB = Integer.parseInt(initSecondLine.split(":")[1]);
        
        boolean ret= false;
        if (hours<hoursB || (hours==hoursB && mins<=minsB)){
            ret = true;
        }
        
        return ret;
    }
    
    public void printSituation(String[] a, String[] b){
        int limit=Math.max(a.length, b.length);
        System.out.println();
        for (int x=0;x<limit;x++){
            if (x<a.length)
                System.out.print(a[x]+" ");
            if (x<b.length)
                System.out.print(b[x]);
            System.out.print("\n");
        }
    }
    
    private void solveCase(int curCase){
        
        //initializes the case vars
        int limA,limB,gap;
        String[] aLines, bLines;
        int aTrains=0, bTrains=0;
        
        int x;
        
        textFile.advanceLine();
        gap = Integer.parseInt(textFile.getCurLine());
        textFile.advanceLine();
        limA = Integer.parseInt(textFile.getCurLine().split(" ")[0]);
        limB = Integer.parseInt(textFile.getCurLine().split(" ")[1]);
        
        aLines = new String[limA];
        bLines = new String[limB];
        
        for (x=0;x<limA;x++){
            textFile.advanceLine();
            aLines[x] = textFile.getCurLine();
        }
        
        for (x=0;x<limB;x++){
            textFile.advanceLine();
            bLines[x] = textFile.getCurLine();
        }
        
        Arrays.sort(aLines);
        Arrays.sort(bLines);
        
        boolean done = false,aHasRoute,bHasRoute,stuckBoth;
        int dest,side;
        int y=0;
        
        dest=-1;
        
        String[] temp = aLines[0].split(" ")[0].split(":");
        x=Integer.parseInt(temp[0]+temp[1]);
        
        temp = bLines[0].split(" ")[0].split(":");
        y=Integer.parseInt(temp[0]+temp[1]);
        
        if (x<=y)
            side=0;
        else
            side=1;
        
        stuckBoth=false;
        
        limA = aLines.length;
        limB = bLines.length;
        int limX,limY;
        
        boolean changed;
        //solves
        while(!done){
            if (side==0){
                limX=aLines.length;
                limY=bLines.length;
            } else {
                limX=bLines.length;
                limY=aLines.length;
            }

            changed = false;
            for (x=0;x<limX;x++)
                for (y=0;y<limY;y++)
                    if (side==0){
                        if (!changed)
                            if(!aLines[x].equals("solved"))
                                if (x!=dest){
                                    if(!bLines[y].equals("solved")){
                                        if(canBeTaken(aLines[x],bLines[y],gap)){
                                            changed = true;
                                            aLines[x]="solved";
                                            if (dest==-1)
                                                aTrains++;
                                            dest = y;
                                        }
                                    }
                                } else {
                                    aLines[x]="solved";
                                }
                    }else {
                        if (!changed)
                            if(!bLines[x].equals("solved"))
                                if (x!=dest){
                                    if(!aLines[y].equals("solved")){
                                        if(canBeTaken(bLines[x],aLines[y],gap)){
                                            changed = true;
                                            bLines[x]="solved";
                                            if (dest==-1)
                                                bTrains++;
                                            dest = y;
                                        }
                                    }
                                } else {
                                    bLines[x]="solved";
                                }
                    }
            
            if(side==0)
                side=1;
            else
                side=0;
            
            if (!changed){
                if (dest==-1){
                    if (stuckBoth){
                        aHasRoute=bHasRoute=false;

                        for (x=0;x<limA;x++){
                            if (!aLines[x].equals("solved")){
                                aHasRoute = true;
                                break;
                            }
                        }

                        if(aHasRoute){
                            aHasRoute=false;
                            for (x=0;x<limA;x++){
                                for (y=0;y<limB;y++){
                                    if(!bLines[y].equals("solved") && !aLines[x].equals("solved"))
                                        if(canBeTaken(aLines[x],bLines[y],gap))
                                            aHasRoute = true;
                                }
                            }
                        }

                        if (!aHasRoute){
                            for (x=0;x<limA;x++){
                                if (!aLines[x].equals("solved")){
                                    aLines[x]="solved";
                                    aTrains++;
                                }
                            }
                            done = true;
                        }

                        for (x=0;x<limB;x++){
                            if (!bLines[x].equals("solved")){
                                bHasRoute = true;
                                break;
                            }
                        }

                        if(bHasRoute){
                            bHasRoute=false;
                            for (x=0;x<limB;x++){
                                for (y=0;y<limA;y++){
                                    if(!bLines[x].equals("solved") && !aLines[y].equals("solved"))
                                        if(canBeTaken(bLines[x],aLines[y],gap))
                                            bHasRoute = true;
                                }
                            }
                        }

                        if (!bHasRoute){
                            for (x=0;x<limB;x++){
                                if (!bLines[x].equals("solved")){
                                    bLines[x]="solved";
                                    bTrains++;
                                }
                            }
                            done = true;
                        }
                    }
                    else stuckBoth=true;
                }
                dest=-1;
            }   
            
        }
        //adds solution
        cases.add(String.valueOf(aTrains+" "+bTrains));
    }
    private void printCase(int curCase){
        System.out.println("Case #"+(curCase+1)+": "+cases.get(curCase));
    }
}
