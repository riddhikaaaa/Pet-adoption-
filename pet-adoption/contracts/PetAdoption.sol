// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PetAdoption {
    struct Pet {
        string name;
        string details;
        string age;
        string petAddress;
        string species;
    }

    mapping(address => Pet) public pets;

    event PetAdopted(address indexed owner, string name, string details, string age, string petAddress, string species);

    function adoptPet(string memory _name, string memory _details, string memory _age, string memory _petAddress, string memory _species) public {
        pets[msg.sender] = Pet(_name, _details, _age, _petAddress, _species);
        emit PetAdopted(msg.sender, _name, _details, _age, _petAddress, _species);
    }

    function getPet(address owner) public view returns (string memory, string memory, string memory, string memory, string memory) {
        Pet memory pet = pets[owner];
        return (pet.name, pet.details, pet.age, pet.petAddress, pet.species);
    }
}
