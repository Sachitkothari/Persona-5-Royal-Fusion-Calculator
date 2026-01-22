#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <limits>
#include "merge.hpp"

int main()
{
    std::string p1Name, p2Name;
    std::cout<< "Enter Persona 1 name: ";
    std::getline(std::cin, p1Name);
    std::cout << "Enter Persona 2 name: ";
    std::getline(std::cin, p2Name);
    std::cout<<calculate(p1Name, p2Name);
    return 0;
}