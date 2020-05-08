#include <iostream>
#include <stack>
#include <vector>

using namespace std;

// Complete the abbreviation function below.
string abbreviation(string a, string b) {
    stack<char> aStack;
    stack<char> bStack;
    for (int i = 0; i < a.size(); i++) aStack.push(a[i]);
    for (int i = 0; i < b.size(); i++) bStack.push(b[i]);

    while (!bStack.empty()) {
        if (bStack.top() == toupper(aStack.top())) {
            bStack.pop(); 
            aStack.pop();
        } else if (isupper(aStack.top())) return "NO";
        else aStack.pop();

        if (aStack.size() < bStack.size()) return "NO";
    }
    for (int i = 0; !aStack.empty(); i++) {
        if (isupper(aStack.top())) return "NO";
        aStack.pop();
    }
    return "YES";
}

int main() {
    string a = "DRFNLZZVHLPZWIupjwdmqafmgkg";
    string b = "DRFNLZZVHLPZWI";
    cout << abbreviation(a, b) << endl;
    return 0;
}