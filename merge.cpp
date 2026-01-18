#include <iostream>
#include <string>
#include "persona_merge_rules.hpp"
#include <fstream>
#include <unordered_map>
#include "persona.hpp"
#include "data_from_json.hpp"
#include <vector>

std::string calulate(std::string persona_A, std::string persona_B)
{
    if (persona_A == persona_B)
    {
        return "Fusion requires two unique personas.";
    }
    std::string resultPersonaArcana = fusionRules.at(persona_A + "+" + persona_B);
    loadPersonaData("static_data/persona_list.json");
    buildLookupTables(personaData);
    int levelPersonaA = personaByName.at(persona_A).level;
    int levelPersonaB = personaByName.at(persona_B).level;
    int resultPersonaLevel = ((levelPersonaA + levelPersonaB)/2) + 1;
    std::vector<Persona> possibleResults = personasByArcana.at(resultPersonaArcana);
    Persona resultPersona {
            "Default",
            "Default",
            999
        };
    for(const auto &p: possibleResults)
    {
        if(p.level >= resultPersonaLevel)
        {
            if(resultPersona.level > p.level)
            {
                resultPersona = p;
            }
        }
    }
    return resultPersona.name;
}