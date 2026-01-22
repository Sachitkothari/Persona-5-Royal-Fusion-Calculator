CXX = g++
CXXFLAGS = -Iinclude -std=c++17 -fPIC
LDFLAGS = -shared

SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o)

all: persona_merger persona.dll

persona_merger: $(OBJ)
	$(CXX) $(OBJ) -o persona_merger.exe

persona.dll: $(OBJ)
	$(CXX) $(LDFLAGS) $(OBJ) -o persona.dll

clean:
	rm -f *.o persona_merger.exe persona.dll
