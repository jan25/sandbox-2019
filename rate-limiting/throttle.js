/**
 * Throttling allows execution of last requested in a given time period
 * All previous requests in this time period are dropped
 * 
 * Exercise for reader: Can you think of a usecase for this?
 */
const throttle = function(fn, waitFor = 100) {
    let timerId = null;
    let lastArgs = [];
    return (...args) => {
        lastArgs = args;
        if (timerId) {
            return;
        }
        timerId = setTimeout(() => {
            timerId = null;
            fn(...lastArgs);
        }, waitFor);
    };
}

const throttled = throttle(console.log);

throttled(1);
throttled(2);
throttled(3);

setTimeout(() => {
    throttled(4);
}, 90);

setTimeout(() => {
    throttled(5);
}, 110);
