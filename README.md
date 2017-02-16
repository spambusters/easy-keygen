# easy-keygen
Proof of concept keygen for a fictional, simple algorithm

## Requirements  
Python 3.6 - (new f string formatting)  

## About
By reading the disassembly of a program, we discover that a fictional company uses a very simple alogrithm for its licensing keys.  

The alogrithm simply adds each ASCII value within the string until a sum of 808 is reached.  
In other words, any string whose ASCII values total 808 will be considered a valid key.  

## Example Output  

```
How many keys do you want? 6  
Found valid key: l0O_Zt75aC  
Found valid key: hiFaP7I9XO  
Found valid key: WmnqegnK  
Found valid key: dfg6Qv_OL  
Found valid key: yMG9ph-on  
Found valid key: QiFlGFLLRE  

Found 6 keys!
```  

After completion, keys are dumped to a local keys.txt file
