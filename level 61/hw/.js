for (let i = 1; i <= 10; i++) {
    console.log("The square of " + i + " is: " + (i * i));
}

let str = "Hello";
for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}

for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}