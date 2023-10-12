// f38d3868-532c-4d70-a522-4aff38ecddef
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int dpSolution(vector<int> &wordLengths, int width, int height, int size, int count)
{
    vector<int> dpArray(width + 1, 0);
    int index = 0;
    int spaceTaken = 0;
    int widthIndex = 0;
    int textCounter = 0;

    do
    {
        if (height >= count)
        {
            int linesFit = height / count; 
            textCounter += linesFit;
            dpArray[widthIndex] = textCounter;      
            spaceTaken = height - (height % count); 
        }
        else
            spaceTaken = 0; 

        while (wordLengths[index] <= height - spaceTaken)
        {
            spaceTaken += wordLengths[index] + 1; 
            index++;
            if (index == size)
            {

                textCounter++;
                index = 0;
                dpArray[widthIndex] = textCounter;
            }
        }

        widthIndex++;
    } while (index != 0 && widthIndex < width);

    int temp = widthIndex;

    while (widthIndex < width)
    {
        dpArray[widthIndex] = textCounter + dpArray[widthIndex - temp];

        widthIndex++;
    }

    return dpArray[width - 1];
}

int main()
{
    int width, height;
    string text;
    size_t pos = 0;

    cin >> width;
    cin >> height;
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

    cout << dpSolution(wordLengths, width, height, wordLengths.size(), count) << endl;

    return 0;
}