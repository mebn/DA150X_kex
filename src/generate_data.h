#pragma once

#include <vector>

struct Task {
    int machine_id;
    int processing_time;
};

class Data {
public:
    std::vector<std::vector<Task>> jobs;
    std::vector<int> machines;

    Data(int num_jobs, int num_machines);
    void generate_data(int num_jobs, int num_machines);
};
