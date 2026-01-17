#include <nlohmann/json.hpp>
#include <fstream>

nlohmann::json personaData;

void loadPersonaData(const std::string& path) 
{ 
    std::ifstream file(path); file >> personaData; 
}