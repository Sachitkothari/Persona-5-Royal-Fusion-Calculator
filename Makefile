CXX = g++
CXXFLAGS = -Iinclude -std=c++17

SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o)

persona_merger: $(OBJ)
	$(CXX) $(OBJ) -o persona_merger

clean:
	rm -f *.o persona_merger
