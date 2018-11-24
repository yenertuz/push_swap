# Push_Swap  

##### Header

__Author:__ Yener Tuz  
__Creation date__: 11/23/2018  

* A 42USA project

##### Intro

A two part project on sorting a list of unsorted integers using two stacks:  
  
__Part 1–checker :__ reads from a a file named `numbers` unsorted integers, and from another file named `ops` instructions on how to sort these integers using two   stacks  
				and outputs `OK` for a successful sort, and `KO` for an unsuccessful sort  
				  
  
__Part 2 –push_swap  :__ reads from a file named `numbers` unsorted integers, and writes into a file named `ops` the intstructions necessary to sort these numbers   using  
				two stacks  
  
* All read numbers will be automatically pushed into the first stack  
* The numbers need to be in sorted order back in the first stack  
* For a list of instructions (ops) see `Ops` below  
* The numbers need to be unique integers separated by a space  
* Any other use is **UNDEFINED**  
  

##### Requirements

a terminal, python3 (❤)

##### Usage

```
$ echo "94 72 12 83 -82 71 45" > "numbers"
$ ./push_swap
$ ./checker
OK
```

##### Ops

* __sa:__ swap a -> swap the first 2 elements at the top of stack a   
* __sb:__ swap b -> swap the first 2 elements at the top of stack b   
* __ss:__ swap both -> sa and sb at the same time   
* __pa:__ push a -> take the first element of the top from the top of stack a and put it to stack b   
* __pb:__ push b -> push a for stack b   
* __ra:__ rotate a -> shift elements in stack a so that the first element becomes the last one   
* __rb:__ rotate b -> rotate a for stack b   
* __rr:__ rotate both -> ra and rb at the same time   
* __rra:__ reverse rotate a -> shift elements in stack a so the last element becomes the first one   
* __rrb:__ reverse rotate b -> rra for stack b   
* __rrr:__ reverse rotate both -> rra and rrb at the same time   

