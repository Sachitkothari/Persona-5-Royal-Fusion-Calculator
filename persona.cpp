#include <string>
#include <unordered_map>
#include <nlohmann/json.hpp>
#include <vector>
#include "persona.hpp"
#include <iostream>
std::unordered_map<std::string, Persona> personaByName;
std::unordered_map<std::string, std::vector<Persona>> personasByArcana;

void buildLookupTables(const nlohmann::json& personaData)
{
    for (const auto &p: personaData)
    {
        Persona persona {
            p["name"],
            p["arcana"],
            p["level"]
        };
        personaByName[persona.name] = persona;
        personasByArcana[persona.arcana].push_back(persona);
    }
}