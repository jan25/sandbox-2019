
const throttle = function(fn, waitFor = 100) {
    let timerId = null;
    return (...args) => {
        if (timerId) {
            return;
        }
        timerId = setTimeout(() => {
            timerId = null;
            fn(...args);
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
