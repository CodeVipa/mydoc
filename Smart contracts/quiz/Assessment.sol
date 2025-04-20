// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract SimpleBank{
    mapping (address=>uint256)private balance;

    function deposit()public payable{
        require(msg.value>=0,'the amount of money can not go below zero');
        balance[msg.sender]+=msg.value;
    }
    function withdraw(uint256 amount)public{
        require(balance[msg.sender]>=amount,'you can now withdraw');
        balance[msg.sender]-=amount;
    }
    function getBalance()public view returns(uint256){
        return balance[msg.sender];
    }
}