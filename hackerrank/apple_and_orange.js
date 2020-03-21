function countApplesAndOranges(s, t, a, b, apples, oranges) {
    let houseStart = s;
    let houseEnd = t;
    let appleTreeLocation = a;
    let orangeTreeLocation = b;
    let applesCount, orangesCount;
    applesCount = orangesCount = 0;

    for (const apple of apples) {
        let appleSum = apple + appleTreeLocation;
        if (appleSum >= houseStart && appleSum <= houseEnd) {
           applesCount++; 
        }
    }

    for (const orange of oranges) {
        let appleSum = orange + orangeTreeLocation;
        if (appleSum >= houseStart && appleSum <= houseEnd) {
           orangesCount++; 
        }
    }
    console.log(applesCount);
    console.log(orangesCount);
}

countApplesAndOranges(7, 11, 5 , 15, [-2 ,2 ,1], [5, -6]);
