#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <vector>
#include "merge.hpp"

int main()
{
    std::string p1Name, p2Name;
    std::cout<< "Enter Persona 1 name";
    std::cin>>p1Name;
    std::cout<< "Enter Persona 2 name";
    std::cin>>p2Name;
    std::cout<<calulate(p1Name, p2Name);
    //std::cout<<"Hello world";
    return 0;
}