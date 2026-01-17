#include <string>
#include <unordered_map>
#include <nlohmann/json.hpp>
#include <vector>

struct Persona {
    std::string name;
    std::string arcana;
    int level;
};

std::unordered_map<std::string, Persona> personaByName;
std::unordered_map<std::string, std::vector<Persona>> personasByArcana;

void buildLookupTables(nlohmann::json personaData)
{
    for (const auto &p: personaData)
    {
        Persona persona {
            p["Name"],
            p["Arcana"],
            p["level"]
        };
        personaByName[persona.name] = persona;
        personasByArcana[persona.arcana].push_back(persona);
    }
}