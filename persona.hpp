#include <string>
#include <unordered_map>
#include <nlohmann/json.hpp>
#include <vector>

struct Persona {
    std::string name;
    std::string arcana;
    int level;
};

extern std::unordered_map<std::string, Persona> personaByName;
extern std::unordered_map<std::string, std::vector<Persona>> personasByArcana;

void buildLookupTables(const nlohmann::json& personaData);