// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Calculator {
    
    // Function to add two numbers
    function add(int256 a, int256 b) public pure returns (int256) {
        return a + b;
    }

    // Function to subtract two numbers
    function subtract(uint a, uint b) public pure returns (uint) {
        return a - b;
    }

    // Function to multiply two numbers
    function multiply(uint a, uint b) public pure returns (uint) {
        return a * b;
    }

    // Function to divide two numbers
    function divide(int a, int b) public pure returns (int) {
        require(b != 0, "Cannot divide by zero");
        return a / b;
    }

    // Function to get the remainder (modulus)
    function modulus(int256 a, int256 b) public pure returns (int256) {
        require(b != 0, "Cannot find modulus with zero");
        return a % b;
    }
}



     

