// SPDX-License-Identifier: MIT
pragma solidity 0.8;
contract helloworld{
    string public a='hello faith';
    
}
contract Calculator{

    //function to add numbers
    function sum(int256 a,int256 b)public pure returns(int256){
        return a+b;
    }
    function substract(int256 a, int256 b)public pure returns(int256){
        return a-b;
    }
    function multiply(int256 a, int256 b)public pure returns(int256){
        return a*b;
    }
    function divide(int256 a,int256 b)public pure returns(int256){
      require(b!=0,"can not divide by 0");
            return a/b;
        }
        function modulus(int256 a,int256 b)public pure returns(int256){
            require(b!=0,"can not get a modulus with zero");
            return  a%b;
        }
    
    }

    contract Message{
        string public message="hello, teacher";
        function setMessage(string _message)public view returns(string memory){
            newmessage=_message;
        }
        function getMessage()public view returns{
            return newmessage;
        }
    }
