// b61a7745-dddf-4d90-a4af-94b9a7a88132
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int dpSolution(vector<int> &wordLengths, int w, int h, int size, int count)
{
    vector<int> dpArray(w + 1, 0);
    int i = 0;
    int spaceTaken = 0;
    int widthIndex = 0;
    int textCounter = 0;

    do
    {
        if (h >= count)
        {
            int linesFit = h / count; 
            textCounter += linesFit;
            dpArray[widthIndex] = textCounter;      
            spaceTaken = h - (h % count); 
        }
        else
            spaceTaken = 0; 

        while (wordLengths[i] <= h - spaceTaken)
        {
            spaceTaken += wordLengths[i] + 1; 
            i++;
            if (i == size)
            {

                textCounter++;
                i = 0;
                dpArray[widthIndex] = textCounter;
            }
        }

        widthIndex++;
    } while (i != 0 && widthIndex < w);

    int temp = widthIndex;

    while (widthIndex < w)
    {
        dpArray[widthIndex] = textCounter + dpArray[widthIndex - temp];

        widthIndex++;
    }

    return dpArray[w - 1];
}

int main()
{
    int w, h;
    string text;
    size_t pos = 0;

    cin >> w;
    cin >> h;
    cin.ignore(); 
    getline(cin, text);
    int count = text.size() + 1;

    vector<int> wordLengths;
    
    while ((pos = text.find(' ')) != std::string::npos)
    {
        wordLengths.push_back(pos); 
        text.erase(0, pos + 1);     
    }
    wordLengths.push_back(text.size()); 

    cout << dpSolution(wordLengths, w, h, wordLengths.size(), count) << endl;

    return 0;
}