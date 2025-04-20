// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GradingSystem{
    function getGrade(uint score)public pure returns(string memory ){
        require(score<=100, "make sure your scores is between 0 and 100");
        if(score>=90){
            return"A";
        }
        else if(score>=80){
            return"B";
        }
        else if(score >= 70){
            return "C";
        }
        else if(score>=60){
            return "D";
        }
        else{
            return "F";
        }
    }
    

}