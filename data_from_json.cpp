#include <nlohmann/json.hpp>
#include <fstream>
#include "data_from_json.hpp"

nlohmann::json personaData;

void loadPersonaData(const std::string& path) 
{ 
    std::ifstream file(path); file >> personaData; 
}