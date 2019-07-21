
const debounce = function(fn, waitFor = 100) {
    let timerId = null;
    return (...args) => {
        if (timerId) {
            clearTimeout(timerId);
        }
        timerId = setTimeout(() => {
            timerId = null;
            fn(...args);
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