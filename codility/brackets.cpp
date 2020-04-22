#include <stack>
#include <iostream>

using namespace std;

int solution(string &S) {
	stack<char> brackets;

	for (int i = 0; i < S.size(); i++) {
		char analyzingChar = S[i];
		if (analyzingChar == '{' || analyzingChar == '[' || analyzingChar == '(') {
			brackets.push(analyzingChar);
		}

		if (analyzingChar == '}' || analyzingChar == ']' || analyzingChar == ')') {
			char analyzingCharOposite;
			if (analyzingChar == '}') {
				analyzingCharOposite = '{';
			} else if (analyzingChar == ']') {
				analyzingCharOposite = '[';
			} else if (analyzingChar == ')') {
				analyzingCharOposite = '(';
			}

			if (brackets.top() == analyzingCharOposite) {
				brackets.pop();
			} else {
				return 0;
			}
		}
	}

	return brackets.empty()? 1: 0;
}


int main() {
	stack<char> brackets;
	string test = "{[()()]}";
	cout << solution(test) << endl;



	return 0;
}