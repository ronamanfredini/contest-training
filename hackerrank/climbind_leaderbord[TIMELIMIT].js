
function climbingLeaderboard(scores, alice) {
    let positions = [];

    for (let i = 0; i < alice.length; i++) {
        let aliceScore = alice[i];
        let rankCounter = 1;
        for (let j = 0; j < scores.length; j++) {
            let currentScore = scores[j];
            if (currentScore < scores[j - 1])
                rankCounter++;
            if (aliceScore >= currentScore) {
                positions.push(rankCounter);
                break;
            }

            if (j == scores.length - 1) {
                if (aliceScore < currentScore) {
                    rankCounter++;
                }
                positions.push(rankCounter);
            }
        }
    }
    return positions;
}