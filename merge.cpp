#include <iostream>
#include <string>
#include "persona_merge_rules.hpp"
#include <fstream>
#include <unordered_map>
#include "persona.hpp"
#include "data_from_json.hpp"
#include <vector>

std::string calculate(std::string persona_A, std::string persona_B)
{
    if (persona_A == persona_B)
    {
        return "Fusion requires two unique personas.";
    }
    loadPersonaData("static_data/persona_list.json");
    buildLookupTables(personaData);
    //for (auto& [name, persona] : personaByName) std::cout << "[" << name << "]\n";
    std::string persona1Arcana = personaByName.at(persona_A).arcana;
    std::string persona2Arcana = personaByName.at(persona_B).arcana;
    std::string arcanaFormula = persona1Arcana + "+" + persona2Arcana;
    if(fusionRules.count(arcanaFormula) == 1)
    {}
    else
    {
        arcanaFormula = persona2Arcana + "+" + persona1Arcana;
    }
    std::string resultPersonaArcana = fusionRules.at(arcanaFormula);
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

extern "C" const char* merge(const char* a, const char* b) {
    std::string result = calculate(a, b);
    char* output = new char[result.size() + 1];
    std::strcpy(output, result.c_str());
    return output;
}