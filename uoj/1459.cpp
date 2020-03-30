#include <iostream>

using namespace std;

int main() {
    int objectsCount, rangeStart, rangeEnd, minRange, maxRange, focusCount;
    while (cin >> objectsCount) {
        minRange = focusCount = maxRange = 0;
        for (int i = 0; i < objectsCount; i++) {
            cin >> rangeStart >> rangeEnd;
            if (i == 0) {
                minRange = rangeStart;
                maxRange = rangeEnd;
                focusCount++;
            }
            if (rangeStart > maxRange) {
                maxRange = rangeStart;
                focusCount++;
            }
            if (rangeEnd < minRange) {
                minRange = rangeEnd;
                focusCount++;
            }
        }
        cout << focusCount << endl;
    }
    
    return 0;
}