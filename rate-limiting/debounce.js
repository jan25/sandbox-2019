/**
 * Debounce waits on a request for a given time period
 * If there is a new request the timer if reset
 * Otherwise, executes the request at end of time period
 * 
 * Exercise for reader: Can you think of a usecase for this?
 */
const debounce = function(fn, waitFor = 100) {
    let timerId = null;
    let lastArgs = [];
    return (...args) => {
        lastArgs = args;
        if (timerId) {
            clearTimeout(timerId);
        }
        timerId = setTimeout(() => {
            timerId = null;
            fn(...lastArgs);
        }, waitFor);
    };
};

const debounced = debounce(console.log);

debounced(1);
debounced(2);
debounced(3);

setTimeout(() => {
    debounced(4);
}, 50);
