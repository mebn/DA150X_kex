#ifndef __POPULATION_H__
#define __POPULATION_H__

#include "include/job_base.h"
#include "include/linked_list.h"
#include "include/chromosome_base.h"
#include "include/machine_base.h"
#include "job.h"
#include "machine.h"


struct evolution_factors_t{
    unsigned int *c_selected1;
    unsigned int *c_selected2;
    unsigned int *cut_points;
    unsigned int *range;

    unsigned int *m_selected;
    unsigned int *gene_idx;
    double *new_genes;
};

struct population_t{
    unsigned int population_number;

    struct {
        int AMOUNT_OF_JOBS;
        int AMOUNT_OF_MACHINES;
        int AMOUNT_OF_CHROMOSOMES;
        int AMOUNT_OF_R_CHROMOSOMES;
        double EVOLUTION_RATE;
        double SELECTION_RATE;
        int GENERATIONS;
    }parameters;

    struct {
        job_t * jobs;
        machine_t * machines;
        process_time_t ** process_times;
    }sample;

    struct{
        job_t ** jobs;
        machine_t **machines;
        process_time_t ** process_times;
        list_operations_t *list_ops;
        job_base_operations_t *job_ops;
        machine_base_operations_t *machine_ops;
    }cuda_objects;

    struct{
        job_t ** address_of_cujobs;
        machine_t ** address_of_cumachines;
        process_time_t **address_of_process_times_entry;    
    }host_objects;

    struct {
        struct{
            int AMOUNT_OF_HOST_CHROMOSOMES;
            chromosome_base_t * chromosomes;
            double **genes;
        }host_chromosome;
        struct{
            chromosome_base_t * chromosomes;
            double **genes;
            double **address_of_cugenes;
        }device_chromosome;
    }chromosomes;

    struct {
        struct evolution_factors_t device;
        struct evolution_factors_t host;
    }evolution_factors;

    double best_fitness_value;
};

void copyResult(struct population_t *pop, char * filename);

void initPopulation(struct population_t * pop);

void swapPopulation(struct population_t pop[], int amount_of_populations);

void *geneticAlgorithm(void * pop);

#endif
