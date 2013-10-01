/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package googlecodejam08;

/**
 *
 * @author diogo
 */
import java.io.*;
import java.util.Scanner;

public class TextScanner {

    String curLine;
    Scanner scanner;

    /**
    * @param aFileName full name of an existing, readable file.
    */
    public TextScanner(String aFileName) throws FileNotFoundException{
        scanner = new Scanner(new File(aFileName));
        curLine = scanner.nextLine();
    }

    public String getCurLine(){
        return curLine;
    }
    
    public boolean advanceLine(){
        if (scanner.hasNextLine()){
            curLine = scanner.nextLine();
            return true;
        }
        else{
            scanner.close();
            return false;
        }
    }
}
