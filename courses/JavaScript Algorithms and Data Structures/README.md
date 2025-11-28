# Javascript Algorithms and Data Structures - freecodeCamp

![](https://img.shields.io/badge/Code-Javascript-informational?style=flat&logo=javascript&logoColor=yellow&color=f0db4f)

https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/

<br>

## Palindrome checker
Returns ````true```` if the provided string is a palindrome. Otherwise, it returns ````false```.

A palindrome is a word or phrase that is spelled the same forwards and backwards, ignoring punctuation, capitalization, lowercase, and spacing.

> Note: You will have to remove all non-alphanumeric characters (punctuation, spaces and symbols) and convert everything to upper or lower case to check for palindromes.

We will pass strings with variable formats, such as ```racecar```, ````RaceCar``` and ````race CAR``` among others.

We will also pass strings with special symbols, such as ````2A3*3a2```, ````2A3 3a2``` and ````2_A3*3#A2```.
[Solution 👩🏻‍💻](../JavaScript%20Algorithms%20and%20Data%20Structures/comprobadorPalindormo.js)

<br>

## Roman numeral converter
Convert the provided number to a Roman numeral.

| Roman numerals | Arabic numerals | |
| --- | --- |
| M | 1000 |
| CM | 900 |
| D | 500 |
| CD | 400 | | C | 100 | 100 | 100
| C | 100 |
| XC | 90
| L | 50 |
| XL | 40 |
| X | 10 |
| IX | 9 | | V | 5 |
| V | 5 |
| IV | 4 | | I | 1 |
| I | 1 |

All Roman numeral answers must be provided in capital letters.
[Solution 👩🏻‍💻](../JavaScript%20Algorithms%20and%20Data%20Structures/conversorRomanos.js)

<br>

## Caesar cipher
One of the simplest and best known ciphers is the Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by a certain amount.

A common modern usage is the ROT13 cipher, where the letter values are shifted by 13 places. So A ↔ N, B ↔ O and so on.

Write a function that receives a ROT13-encoded string as input and returns a decoded string.

All letters will be uppercase. Do not transform any non-alphabetic characters (spaces, punctuation, for example), but do transmit them.
[Solution 👩🏻‍💻](../JavaScript%20Algorithms%20and%20Data%20Structures/cifradoCesar.js)

<br>

## Phone number validator 

Returns ````true``` if the string passed matches a valid US phone number.

The user can fill in the form field in any way he chooses, as long as it is in the format of a valid US number. The following are examples of valid formats for US numbers (see the tests below for other variants):

```
555-555-5555
(555)555-5555
(555) 555-5555
555 555 5555
5555555555
1 555 555 5555
```

For this challenge you will be presented with a string such as 800-692-7753 or 8oo-six427676;laskdjf. Your job is to validate or reject the US phone number based on any combination of the formats provided above. The area code is required. If the country code is provided, you must confirm that the country code is 1. Return true if the string is a valid US phone number; otherwise return false.
[Solution 👩🏻‍💻](../JavaScript%20Algorithms%20and%20Data%20Structures/validadorNumerosTelefonicos.js)

<br>

## Cash register

Design a function checkCashRegister() that accepts the purchase price as the first argument (price), the amount paid as the second argument (cash), and the cash held by the cash register (cid) as the third argument.

cid is a 2D array that lists the available currencies.

The checkCashRegister() function must always return an object with a status key and a change key.

It returns {status: "INSUFFICIENT_FUNDS", change: []} if the cash on hand is less than the change needed, or if you cannot return exact change.

Returns {status: "CLOSED", change: [...]} if the cash on hand as value of the change key is equal to the change due.

In any other case, returns {status: "OPEN", change: [...]}, with the change to be delivered in coins and banknotes, sorted from highest to lowest, as change key value.

Currency Unit | Amount | |
| --- | --- |
| Penny | $0.01 (PENNY) |
| | Nickel | $0.05 (NICKEL) | |
Dime | | $0.1 (DIME) |
| Quarter $0.25 (QUARTER)
| Dollar | $1 (ONE) |
| Five Dollars | $5 (FIVE) |
Ten Dollars | $10 (TEN) | $10 (TEN) | $10 (TEN)
| $20 (TWENTY) | Twenty Dollars | $20 (TWENTY) |
One-hundred Dollars | $100 (ONE HUNDRED) | $100 (ONE HUNDRED) | $100 (ONE HUNDRED) | $100 (ONE HUNDRED)

The following is an example of cash on hand in arrangement format:

```
[
  ["PENNY", 1.01],
  ["NICKEL", 2.05],
  ["DIME", 3.1],
  ["QUARTER", 4.25],
  ["ONE", 90],
  ["FIVE", 55],
  ["TEN", 20],
  ["TWENTY", 60],
  ["ONE HUNDRED", 100]
]
```
[Solution 👩🏻‍💻](../JavaScript%20Algorithms%20and%20Data%20Structures/cajaRegistradora.js)