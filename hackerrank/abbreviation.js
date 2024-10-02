// URL - https://www.hackerrank.com/challenges/abbr/problem

function checkStrings(a, b, memo) {
    if (memo.has(a)) {
        return memo.get(a);
    }

    if (a.toUpperCase() === b.toUpperCase()) {
        return true;
    }

    if (a.length < b.length) {
        return false;
    }

    for (let i = 0; i < a.length; i++) {
        if (a[i] === a[i].toLowerCase()) {
            const newA = a.slice(0, i) + a.slice(i + 1);
            let result = checkStrings(newA, b, memo)
            if (result) {
                return true;
            } else {
                memo.set(a, false);
            }
        }
    }

    return false;
}

function abbreviation(a, b) {
    const memo = new Map();
    return checkStrings(a, b, memo) ? 'YES' : 'NO';
}


console.log(abbreviation('AbcDE', 'ABDE'));