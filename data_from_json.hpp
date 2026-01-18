#include <nlohmann/json.hpp>
#include <fstream>

extern nlohmann::json personaData;

void loadPersonaData(const std::string& path);