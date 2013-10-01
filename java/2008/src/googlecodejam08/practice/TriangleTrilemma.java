/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package googlecodejam08.practice;

import googlecodejam08.*;
import java.awt.Polygon;
import java.io.FileNotFoundException;
import java.util.Vector;
import javax.media.j3d.PolygonAttributes;

/**
 *
 * @author Diogo Luiz Böhm
 */
public class TriangleTrilemma {
    TextScanner textFile;
    Vector<String> cases;
    int caseCount;
    
    
    public TriangleTrilemma(String string) throws FileNotFoundException {
        textFile = new TextScanner(string);
        caseCount = Integer.parseInt(textFile.getCurLine());
        cases = new Vector<String>();
        for(int x=0;x<caseCount;x++){
            this.solveCase(x+1);
            this.printCase(x);
        }
    }
    
    private int det(int xa,int ya, int xb, int yb, int xc, int yc){
        return ((xb-xa) * (yc-ya)) - ((xc-xa) * (yb-ya));
    }
    
    private int skal(int xa,int ya, int xb, int yb, int xc, int yc){
        return (xb-xa) * (xc-xa) - (yc-ya) * (yb-ya);
    }
    /*
     * X - 3 equal Xs or 3 equal Ys won't form a triangle;
     * 3 different size lenghts = scalene
     * 2 equal size lengths = isosceles
     * 
     * 1 angle > 90° = obtuse
     * 3 angles < 90° = acute
     * 1 angle == 90° = rectangle
     */
    private void solveCase(int curCase){
        textFile.advanceLine();
        String[] coords = textFile.getCurLine().split(" ");
        String thisCase = "";
        
        
        
        int xa = Integer.parseInt(coords[0]),ya = Integer.parseInt(coords[1]);
        int xb = Integer.parseInt(coords[2]),yb = Integer.parseInt(coords[3]);
        int xc = Integer.parseInt(coords[4]),yc = Integer.parseInt(coords[5]);
        /*
        double length1 = Math.sqrt(((xa-xb)*(xa-xb))+((ya-yb)*(ya-yb)));
        double length2 = Math.sqrt(((xa-xc)*(xa-xc))+((ya-yc)*(ya-yc)));
        double length3 = Math.sqrt(((xb-xc)*(xb-xc))+((yb-yc)*(yb-yc)));
        
        double thetaA = (Math.acos((Math.pow(length1,2)-Math.pow(length3,2)-Math.pow(length2,2))/(-2*length2*length3)) * (180 / Math.PI));
        double thetaC = (Math.acos((Math.pow(length3, 2) - Math.pow(length1, 2) - Math.pow(length2, 2)) / (-2 * length1 * length2)) * (180 / Math.PI));
        //double thetaB = (Math.acos((Math.pow(length1, 2) - Math.pow(length2, 2) - Math.pow(length3, 2)) / (-2 * length1 * length3)) * (180 / Math.PI));
        double thetaB =(180-thetaA-thetaC);
        */
        if (det(xa,ya,xb,yb,xc,yc)!=0){
            thisCase = "scalene";
            if (skal(xa,ya,xb,yb,xb,yb) == skal(xa,ya,xc,yc,xc,yc))
                thisCase = "isosceles";
            if (skal(xc,yc,xb,yb,xb,yb) == skal(xa,ya,xc,yc,xc,yc))
                thisCase = "isosceles";
            if (skal(xa,ya,xb,yb,xb,yb) == skal(xb,yb,xc,yc,xc,yc))
                thisCase = "isosceles";
            
            //System.out.println("\n"+thetaA+" "+thetaB+" "+thetaC+" ");

            int c = skal(xa,ya,xb,yb,xc,yc);
            if (c==0) 
                thisCase= thisCase+" right";
            else if (c<0)
                thisCase= thisCase+" obtuse";
            else
                thisCase= thisCase+" acute";
            /*
            if (Math.round(thetaA)==90.0000000 || Math.round(thetaB)==90.0000000 || Math.round(thetaC)==90.0000000){
                thisCase= thisCase+" right";
            } else if (thetaA>90.0000000 || thetaB>90.0000000 || thetaC>90.0000000){
                thisCase= thisCase+" obtuse";
            } else {
                thisCase= thisCase+" acute";
            }
             * */
        } else {
            thisCase = "not a";
        }
        
        thisCase = thisCase +" triangle";
        cases.add(thisCase);
    }
    
    private void printCase(int curCase){
        System.out.println("Case #"+(curCase+1)+": "+cases.get(curCase));
    }
}
