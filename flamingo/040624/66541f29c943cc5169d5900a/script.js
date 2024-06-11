const readlineSync = require('readline-sync');

function max_powered_rooms(M, N, K, F, correct_wirings) {
    let dp = new Array(M + 1);
    for (let i = 0; i <= M; i++) {
        dp[i] = new Array(F + 1);
        for (let j = 0; j <= F; j++) {
            dp[i][j] = new Array(K + 1).fill(0);
        }
    }

    for (let i = 1; i <= M; i++) {
        for (let j = 0; j <= F; j++) {
            for (let k = 0; k <= K; k++) {
                if (k > i || j > i) continue;
                let activated = correct_wirings[i - 1] + dp[i - 1][j][k];
                let deactivated = (N - correct_wirings[i - 1]) + (k > 0 && j > 0 ? dp[i - 1][j - 1][k - 1] : 0);

                dp[i][j][k] = Math.max(activated, deactivated);
            }
        }
    }

    return dp[M][F][K];
}

function getInput() {
    let M = parseInt(readlineSync.question("Enter the number of floors: "));
    let N = parseInt(readlineSync.question("Enter the number of rooms per floor: "));
    let K = parseInt(readlineSync.question("Enter the exact number of master switches to be deactivated: "));
    let F = parseInt(readlineSync.question("Enter the maximum number of floors that can be left without power completely: "));

    let correct_wirings = [];
    for (let i = 0; i < M; i++) {
        let wiring = parseInt(readlineSync.question(`Enter the number of correctly wired rooms on floor ${i + 1}: `));
        correct_wirings.push(wiring);
    }

    return { M, N, K, F, correct_wirings };
}

function main() {
    const { M, N, K, F, correct_wirings } = getInput();
    console.log(max_powered_rooms(M, N, K, F, correct_wirings));
}

main();

