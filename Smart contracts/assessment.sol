// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract SimpleBank{
    mapping (address=>uint256)private balance;
    event Deposit(address indexed  user,uint256 amount);
    event Withdraw(address indexed  user,uint256 amount);

    function deposit()public payable{
        require(msg.value>=0,'the amount of money can not go below zero');
        balance[msg.sender]+=msg.value;
        emit Deposit(msg.sender, msg.value);
    }
    function withdraw(uint256 amount)public{
        require(balance[msg.sender]>=amount,'you can not withdraw with that amount how about you deposit some more?');
        balance[msg.sender]-=amount;
        emit Withdraw(msg.sender, amount);
    }
    function getBalance()public view returns(uint256){
        return balance[msg.sender];
    }
}