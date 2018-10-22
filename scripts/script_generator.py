# (c)2018 Andreas Seiderer

from os import listdir
import os
from os.path import isfile, join

if False:
    file_list_dir = "lists/generated/daisy_increment"

    f = open("run_lists_daisy_increment.sh", "w")

    onlyfiles = [f for f in listdir(file_list_dir) if isfile(join(file_list_dir, f))]

    for listfile in onlyfiles:
        neuronalNetHub = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/1"
        neuronalNet = "mobilenet_v2_100_128"
        trainingsteps = 1000
        listfilename = os.path.splitext(os.path.basename(listfile))[0]
        log_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + ".txt"
        out_graph_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + ".pb"
        intermediate_graph_dir = "intermediate_graph/" + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)
        labels_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + "_output_labels.txt"
        retrain_logs_dir = "retrain_logs/"  + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)
        bottleneck_dir = "bottleneck_flower"
        saved_model_dir = "saved_model/" + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)

        command = "python retrain_hub_filelists.py " \
                  "--image_list {} " \
                  "--how_many_training_steps {} " \
                  "--log_file_name {} " \
                  "--tfhub_module {} " \
                  "--output_graph {} " \
                  "--intermediate_output_graphs_dir {} " \
                  "--output_labels {} " \
                  "--summaries_dir {} " \
                  "--bottleneck_dir {} " \
                  "--saved_model_dir {}".format(file_list_dir+"/"+listfilename+".tsv", trainingsteps, log_file_name, neuronalNetHub, out_graph_file_name, intermediate_graph_dir, labels_file_name, retrain_logs_dir, bottleneck_dir, saved_model_dir)

        f.write(command+"\n")
    f.close()


if False:
    file_list_dir = "lists/generated/all_increment"

    f = open("run_lists_all_increment.sh", "w")

    onlyfiles = [f for f in listdir(file_list_dir) if isfile(join(file_list_dir, f))]

    for listfile in onlyfiles:
        neuronalNetHub = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/1"
        neuronalNet = "mobilenet_v2_100_128"
        trainingsteps = 1000
        listfilename = os.path.splitext(os.path.basename(listfile))[0]
        log_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + ".txt"
        out_graph_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + ".pb"
        intermediate_graph_dir = "intermediate_graph/" + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)
        labels_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + "_output_labels.txt"
        retrain_logs_dir = "retrain_logs/"  + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)
        bottleneck_dir = "bottleneck_flower"
        saved_model_dir = "saved_model/" + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)

        command = "python retrain_hub_filelists.py " \
                  "--image_list {} " \
                  "--how_many_training_steps {} " \
                  "--log_file_name {} " \
                  "--tfhub_module {} " \
                  "--output_graph {} " \
                  "--intermediate_output_graphs_dir {} " \
                  "--output_labels {} " \
                  "--summaries_dir {} " \
                  "--bottleneck_dir {} " \
                  "--saved_model_dir {}".format(file_list_dir+"/"+listfilename+".tsv", trainingsteps, log_file_name, neuronalNetHub, out_graph_file_name, intermediate_graph_dir, labels_file_name, retrain_logs_dir, bottleneck_dir, saved_model_dir)

        f.write(command+"\n")
    f.close()

if True:
    for i in range(0, 3):
        file_list_dir = "lists/generated/random_increment/{}".format(i)

        f = open("run_lists_random_increment{}.sh".format(i), "w")

        onlyfiles = [f for f in listdir(file_list_dir) if isfile(join(file_list_dir, f))]

        for listfile in onlyfiles:
            neuronalNetHub = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_128/feature_vector/1"
            neuronalNet = "mobilenet_v2_100_128"
            trainingsteps = 1000
            listfilename = os.path.splitext(os.path.basename(listfile))[0]
            log_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + ".txt"
            out_graph_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + ".pb"
            intermediate_graph_dir = "intermediate_graph/" + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)
            labels_file_name = neuronalNet + "_" + listfilename + "_" + str(trainingsteps) + "_output_labels.txt"
            retrain_logs_dir = "retrain_logs/"  + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)
            bottleneck_dir = "bottleneck_flower"
            saved_model_dir = "saved_model/" + neuronalNet + "_" + listfilename + "_" + str(trainingsteps)

            command = "python retrain_hub_filelists.py " \
                      "--image_list {} " \
                      "--how_many_training_steps {} " \
                      "--log_file_name {} " \
                      "--tfhub_module {} " \
                      "--output_graph {} " \
                      "--intermediate_output_graphs_dir {} " \
                      "--output_labels {} " \
                      "--summaries_dir {} " \
                      "--bottleneck_dir {} " \
                      "--saved_model_dir {}".format(file_list_dir+"/"+listfilename+".tsv", trainingsteps, log_file_name, neuronalNetHub, out_graph_file_name, intermediate_graph_dir, labels_file_name, retrain_logs_dir, bottleneck_dir, saved_model_dir)

            f.write(command+"\n")
        f.close()
