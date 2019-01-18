// Just some Basic F# Programs

// FizzBuzz
let FizzBuzz x = // Control flow!
    if x % 15 = 0 then
        printfn "FizzBuzz"
    elif x % 3 = 0 then
        printfn "Fizz"
    elif x % 5 = 0 then
        printfn "Buzz"
    else
        printfn "%i" x;;

let sumOfBuzz n =
    [1..n] |> List.map FizzBuzz;;
    
// Pipeline syntax
let listOfCube N = 
    [1..N] |> List.map cube;;

let sumOfCube N =
    [1..N] |> List.map cube |> List.sum;;

// Euler Problem 1
let Is3Or5 x = (x % 3 = 0 or || % 5 = 0);; 

let SumOf35 N = 
    List.filter Is3Or5 [1..N] |> List.sum;; 
