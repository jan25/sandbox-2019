/**
 * Time Bucketed algorithm
 * Bucket = limit + timeInterval
 * 
 * Allows a maximum of limit number of requests during a timeInterval
 * Requests above this limit are dropped
 */
const limiter = function(fn, limit = 10, bucketIntervalMs = 1000) {
    let firstRequestAt = null; // ms
    let currentLimit = limit;
    const limitInterval = bucketIntervalMs;

    const expired = () => {
        const timeDiff = (Date.now() - firstRequestAt);
        return timeDiff > limitInterval;
    };

    const reset = () => {
        console.log('resetting..');
        currentLimit = limit;
        firstRequestAt = null;
    };

    return (...args) => {
        if (!firstRequestAt) {
            firstRequestAt = Date.now();
        } else if (expired()) {
            reset();
            return;
        }

        if (currentLimit <= 0) {
            console.log('limiting this one');
            return;
        }

        currentLimit--;
        fn(...args);
    };
};

const handler = limiter(console.log);

for (let i = 0; i < 30; ++i) {
    ((i) => {
        setTimeout(() => {
            handler(i);
        }, i * 50);
    })(i);
}
