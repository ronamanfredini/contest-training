function gradingStudents(grades) {
    let resultingGrades = [];
    for (let i = 0; i < grades.length; i++) {
        if (grades[i] < 38) {
            resultingGrades.push(grades[i]);
            continue;
        }

        if ((grades[i] + 2) % 5 == 0) {
            resultingGrades.push(grades[i] + 2);
            continue;
        }
        if ((grades[i] + 1) % 5 == 0) {
            resultingGrades.push(grades[i] + 1);
            continue;
        }
        resultingGrades.push(grades[i]);
    }
    return resultingGrades;
}
