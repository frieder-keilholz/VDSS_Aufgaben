// Algorithmus zur Lösung von Aufgabe 1
// Implementiert von Julia Reinke und Frieder Keilholz

// Die Ergebnisse sind unsortiert, da die Datenstruktur
//  in der die Seiten gespeichert werden unsortiert ist.
// Die Laufzeit der unordered_map ist mit O(1) besser
//  als die der (stabilen) map mit O(log(n))

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

// Hilfsfunktion
// Nimmt String und extrahiert die Seitennamen
vector<char> split(std::string lineIn){
    vector<char> returnVector;
    bool firstSpace = false;
    for(int i = 0; i < lineIn.length(); i++)
    {
        char currChar = lineIn[i];
        
        if(firstSpace == false){
            if(currChar == ' '){
                firstSpace = true;
            }
        }else{
            if(currChar != ' '){
                returnVector.push_back(currChar);
            }
        }
    }
    return returnVector;
}

int main()
{
    std::ifstream infile("Aufgabenblatt-1_Outlinks.txt");
    std::string line;
    vector<char> splitted;
    unordered_map<char, u_long> inlinks_table;

    cout << "Input: " << endl;
    while (std::getline(infile, line))
    {
        cout << line << endl;
        splitted = split(line);
        for(int i = 0; i < splitted.size(); i++){
            inlinks_table[splitted[i]]++;
        }
    }

    cout << endl << "Counted Inlinks:";
    for(auto kv : inlinks_table) 
    {
        cout << endl << "Page: " << kv.first << " Inlinks: " << kv.second;
    }
    cout << endl;
    
    return 1;
}

