/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package googlecodejam08.practice;
import googlecodejam08.TextScanner;
import java.io.FileNotFoundException;

/**
 *
 * @author diogo
 */
public class InputGenerator {
    int cases;
    
    int queries;
    String[] searchEngines;
    String[] preset = {"A9",
"About",
"Accoona",
"Acronymfinder",
"Aftervote",
"Ajaxwhois",
"Alexa",
"AllPlus",
"Alltheweb",
"Altavista",
"Answers",
"AOL",
"Archive,",
"Ask",
"Azoos",
"Beaucoup",
"Better",
"Blinkx",
"Brainboost",
"Buzzle",
"ChaCha",
"Clusty",
"Collarity",
"Complete",
"Country",
"Digital-librarian",
"DMOZ",
"Dogpile",
"Draze",
"Ebingbong",
"Eurekster",
"ExaleadSuperb",
"ExciteDoes",
"Factbites",
"FaganFinder",
"Fazzle",
"Feedster",
"Findsounds",
"FinQoo",
"Freesearch",
"Galaxy",
"Google",
"Healia",
"Hotbot",
"IAF",
"iBoogie",
"Icerocket",
"Illumirate",
"InfoMine",
"Infopeople",
"Infoservice",
"Intute",
"Irazoo",
"Ixquick",
"Jayde",
"Jux2",
"Kartoo",
"Kazazz",
"KidsclickChildren's",
"Librarians",
"Linkopedia",
"Live",
"Lycos",
"Mahalo",
"MammaMulti",
"Mastersite",
"Metacrawler",
"Monstercrawler",
"Mooter",
"MsDewey",
"Oaister",
"Omnimedicalsearch",
"Peerbot",
"Pepesearch",
"Pinakes",
"Questfinder",
"Quintura",
"RedZee",
"Re-quest",
"Scandoo",
"Scirus",
"Scrubtheweb",
"Search-beat",
"Searchbug",
"Search.com",
"Searchhippo",
"Searchy",
"Searchmash",
"Search",
"Searchthe.net",
"Searchtheweb",
"Selectsurf",
"Similicio.us",
"Silobreaker",
"Slider",
"Smartlinks",
"SMEALSearch",
"Sproose",
"Sunsteam",
"Supercrawler"};
    
    public InputGenerator(int cases, int nSearchEngines, int nQueries) throws FileNotFoundException{
        searchEngines = new String[nSearchEngines];
        
        int c,x;
        
        System.out.println("--------- Input Start ----------");
        System.out.println(cases);
        
        for(c=0;c<cases;c++){
            System.out.println(nSearchEngines);
            for (x=0;x<nSearchEngines;x++){
                searchEngines[x]=preset[x];
                System.out.println(searchEngines[x]);
            }
            
            System.out.println(nQueries);
            for (x=0;x<nQueries;x++){
                System.out.println(searchEngines[(int) (Math.random()*100)%nSearchEngines]);
            }
        }
    }
}
