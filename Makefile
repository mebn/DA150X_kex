cuda: src/main.cu
	nvcc --std=c++11 src/main.cu

cpu: src/main.cpp
	g++ --std=c++11 src/main.cpp

cpu-prof: src/main.cpp
	g++ --std=c++11 src/main.cpp -pg