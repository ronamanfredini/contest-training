#include <iostream>
#include <vector>
#define LADDER_ACTIVATED_TIME 10
using namespace std;

int main() {

	vector<int> tempos;
	int tempo, pessoas, nextTempo, totalTempo, timeStop;
	while (cin >> pessoas) {
		if (pessoas == 0) {
			break;
		}
		totalTempo = 0;

		for (int i = 0; i < pessoas; i++) {
			cin >> tempo;
			int timePlusTimeLadderActivated = tempo + LADDER_ACTIVATED_TIME;
			if (i == 0) {
				timeStop = timePlusTimeLadderActivated;
				totalTempo += LADDER_ACTIVATED_TIME;
			} else if (timePlusTimeLadderActivated > timeStop && timeStop > tempo) {
				totalTempo += timePlusTimeLadderActivated - timeStop;
				timeStop = timePlusTimeLadderActivated - timeStop;
			} else if (tempo > timeStop) {
				timeStop = tempo + LADDER_ACTIVATED_TIME;
				totalTempo += LADDER_ACTIVATED_TIME;
			}
		}
		cout << totalTempo << endl;

	}
	return 0;
}