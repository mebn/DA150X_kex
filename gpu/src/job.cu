#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_runtime_api.h>
#include <private/job.h>
#include <string.h>
#include <iostream>
#include <set>

using namespace std;

set<string> createJob(job_t *job, std::map<std::string, std::string> elements)
{
    job->base.job_no = stoul(elements["EP"]);
    job->base.arriv_t = stod(elements["ARRIV_T"]);
    job->base.end_time = job->base.start_time = 0;
    job->base.qty = stoul(elements["QTY"]);

    job->r_qt = stod(elements["R_QT"]) * 60;
    job->recipe.ul_recipe = 0;
    strncpy(job->recipe.str_recipe, elements["RECIPE"].c_str(), 6);
    job->urgent = stod(elements["URGENT_W"]);
    // cout<<elements["CANRUN_TOOL"]<<endl;
    string can_run_tools = elements["CANRUN_TOOL"];
    string temp;
    set<string> v_tools;
    size_t start_pos = 0;
    do {
        temp = can_run_tools.substr(start_pos, 6);
        v_tools.insert(temp);
        start_pos += 6;
        cout << temp << endl;
    } while (start_pos != can_run_tools.length());
    job->base.size_of_process_time = v_tools.size();

    return v_tools;
}

__device__ __host__ double jobGetValue(void *_self)
{
    list_ele_t *self = (list_ele_t *) _self;
    job_t *j = (job_t *) self->ptr_derived_object;
    return *(j->base.os_seq_gene);
}

__device__ __host__ void initJob(job_t *self)
{
    _list_init(&self->list);
    self->list.ptr_derived_object = self;
    self->list.get_value = jobGetValue;

    job_base_init(&self->base);
    self->base.ptr_derived_object = self;
}
