"use strict";
const sieve = (count) => {
    const natural = Array(count + 1).fill(true).fill(false, 0, 2);
    const prime = [];
    for (var i = 2; i < Math.sqrt(count); i++) {
        if (natural[i]) {
            prime.push(i);
            for (let j = i ** 2; j <= (count + 1); j += i) {
                natural[j] = false;
            }
        }
    }
    for (let k = i; k <= (count + 1); k++) {
        if (natural[k]) {
            prime.push(k);
        }
    }
    return prime;
};
console.log(sieve(parseInt(process.argv[2])).toString());
//# sourceMappingURL=sieve.js.map