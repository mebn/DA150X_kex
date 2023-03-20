#include <iostream>
#include <vector>
#include <stdlib.h>
#include "generate_data.h"

// https://developers.google.com/optimization/scheduling/job_shop

Data::Data(int num_jobs, int num_machines) {
    this->machines.resize(num_machines, 0);
    
    generate_data(num_jobs, num_machines);
}

void Data::generate_data(int num_jobs, int num_machines) {
    
}
