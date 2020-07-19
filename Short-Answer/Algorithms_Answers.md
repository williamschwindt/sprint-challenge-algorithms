#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) the runtime will be linear because the loop will run n times


b) O(n^2) nested loops. The inner loop will run n times for every outer loop run and the outer loop will run n times


c) O(n) this is a recursive function that will call itself n times and return when n reaches 0

## Exercise II
The most effiecient way to find floor f would to use binary search. The first step would to find a middle floor 
by dividing the total floors by two. Then throw an egg off to see if it breaks. If it breaks then we can ignore 
any floor above that because it will obviously break on a higher floor. Now find a new middle while ignoring all 
floors above the floor you just dropped an egg from. Throw an egg off, if it breaks repeat the last step if it doesnt
then ignore all floors below that floor and recalculate the middle. Repeat this process until floor f has been found.

This would be a O(log n) solution because the ammount of floors we are searching is halved every time.

