CXX      := g++
CXXFLAGS := -std=c++17 -Wall -Wextra $(shell pkg-config --cflags raylib)
LDFLAGS  := $(shell pkg-config --libs raylib)

SRC      := main.cpp
BIN      := main

all: $(BIN)

$(BIN): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(BIN) $(SRC) $(LDFLAGS)

clean:
	rm -f $(BIN)

.PHONY: all clean
