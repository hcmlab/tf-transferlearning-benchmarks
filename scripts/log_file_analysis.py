# (c)2018 Andreas Seiderer

import datetime


def main():
    total_prog_runtime = None
    total_bottleneck_runtime = None
    total_train_runtime = None
    total_eval_runtime = None

    model_test_accuracy = None

    '''
    flower_inceptionv3_1000steps.txt
    
    flower_mobilenet_v1_100_224_1000steps.txt
    flower_mobilenet_v1_100_128_1000steps.txt
    
    flower_mobilenet_v1_075_224_1000steps.txt
    flower_mobilenet_v1_075_128_1000steps.txt
    
    
    flower_mobilenet_v2_140_224_1000steps.txt
    
    flower_mobilenet_v2_100_224_1000steps.txt
    flower_mobilenet_v2_100_128_1000steps.txt
    flower_mobilenet_v2_100_96_1000steps.txt
    
    flower_mobilenet_v2_075_224_1000steps.txt
    flower_mobilenet_v2_075_128_1000steps.txt
    '''

    for configname in ["flower_inceptionv3_1000steps",
                       "flower_mobilenet_v1_100_224_1000steps",
                       "flower_mobilenet_v1_100_128_1000steps",
                       "flower_mobilenet_v1_075_224_1000steps",
                       "flower_mobilenet_v1_075_128_1000steps",
                       "flower_mobilenet_v2_140_224_1000steps",
                       "flower_mobilenet_v2_100_224_1000steps",
                       "flower_mobilenet_v2_100_128_1000steps",
                       "flower_mobilenet_v2_100_96_1000steps",
                       "flower_mobilenet_v2_075_224_1000steps",
                       "flower_mobilenet_v2_075_128_1000steps"]:
        for run in range(1,4):

            print("config: %s - %s" % (configname, run))

            log_file = open("../measurements/tf1.7_retrain/flower/pi3/%s/%s.txt" % (run, configname), 'r')

            while True:
                line = log_file.readline()
                cols = line[:-1].split("\t")

                if len(cols) == 3:
                    try:
                        date = datetime.datetime.strptime(cols[0], "%Y-%m-%dT%H:%M:%S.%f")
                    except ValueError:
                        date = datetime.datetime.strptime(cols[0], "%Y-%m-%dT%H:%M:%S")

                    func = cols[1]
                    stat = cols[2]

                    if func == "program":
                        if stat == "begin":
                            total_prog_runtime = date
                        elif stat == "end":
                            total_prog_runtime = date - total_prog_runtime
                    elif func == "train":
                        if stat == "begin":
                            total_train_runtime = date
                        elif stat == "end":
                            total_train_runtime = date - total_train_runtime
                    elif func == "model_eval":
                        if stat == "begin":
                            total_eval_runtime = date
                        elif stat == "end":
                            total_eval_runtime = date - total_eval_runtime
                    elif func == "bottlenecks_create_load":
                        if stat == "begin":
                            total_bottleneck_runtime = date
                        elif stat == "end":
                            total_bottleneck_runtime = date - total_bottleneck_runtime

                elif len(cols) == 4:
                    func = cols[1]
                    if func == "model_test_acc_N":
                        model_test_accuracy = cols[2]
                if not line:
                    break
            log_file.close()

            '''print("total: %s" % (total_prog_runtime.total_seconds()))
            print("-> total bottlenecks: %s" % (total_bottleneck_runtime.total_seconds()))
            print("-> total train: %s" % (total_train_runtime.total_seconds()))
            print("-> total eval: %s" % (total_eval_runtime.total_seconds()))'''

            print("%s\n%s\n%s" % (total_bottleneck_runtime.total_seconds(), total_train_runtime.total_seconds(), total_eval_runtime.total_seconds()))
            print("%s" % (model_test_accuracy))


if __name__ == "__main__":
    main()
