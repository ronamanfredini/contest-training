#include <iostream>
#include <string>

using namespace std;

int recursiveSum(int num, int steps, string initialNum) {
    if (initialNum == "0") return 1;

    string numAsString = to_string(num);
    if (numAsString.size() == 1) {
        numAsString = '0' + numAsString;
    }

    int digitSum = (numAsString[0] - '0') + (numAsString[1] - '0');
    string digitSumAsString = to_string(digitSum);

    
    string newNum = "";
    newNum.push_back(numAsString[1]);

    if (digitSumAsString.size() == 1) {
        newNum.push_back(digitSumAsString[0]);
    } else {
        newNum.push_back(digitSumAsString[1]);
    }

    if (newNum.compare(initialNum) == 0) {
        return ++steps;
    } else {
        return recursiveSum(stoi(newNum), ++steps, initialNum);
    }
}

int main() {
    int initialNum;
    while (cin >> initialNum) {
        cout << recursiveSum(initialNum, 0, to_string(initialNum)) << endl;
    }
    return 0;
}