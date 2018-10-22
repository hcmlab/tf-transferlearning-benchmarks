# (c)2018 Andreas Seiderer

import pandas as pd
import os
import secrets

if not os.path.exists("lists/generated/daisy_increment/"):
    os.makedirs("lists/generated/daisy_increment/")

if not os.path.exists("lists/generated/all_increment/"):
    os.makedirs("lists/generated/all_increment/")

df = pd.read_csv("lists/flower_photos_list_default.tsv", header=None, sep="\t")

# remove duplicates (by filename)
df.drop_duplicates(subset=0, keep='first', inplace=True)
df.reset_index(inplace=True, drop=True)

# columns:      0       1      2
#           filename, type, dataset

# daisy increment ------------------------------------------------------------------------------------------------------

if False:
    for i in range(0, 135, 5):
        df1 = df.copy()

        flowers = {
            "daisy":        {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "dandelion":    {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "roses":        {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "sunflowers":   {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "tulips":       {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
        }

        # split
        # 80% training
        # 20% validation

        total_cnt = {}

        for key in flowers:
            if key == "daisy":
                flowers[key]["total_cnt"] = 20+i
                flowers[key]["train_cnt"] = int((flowers[key]["total_cnt"] / 100) * 80)
                flowers[key]["val_cnt"] = int((flowers[key]["total_cnt"] / 100) * 20)
                total_cnt[key] = 400 + flowers[key]["total_cnt"]  # including test with 400 files
            else:
                flowers[key]["total_cnt"] = 150
                flowers[key]["train_cnt"] = int((flowers[key]["total_cnt"] / 100) * 80)
                flowers[key]["val_cnt"] = int((flowers[key]["total_cnt"] / 100) * 20)
                total_cnt[key] = 400 + flowers[key]["total_cnt"]  # including test with 400 files

        for index, row in df1.iterrows():
            flower = row[1]
            if flowers[flower]["cnt"] >= total_cnt[flower]:
                df1.drop([index], inplace=True)
            else:
                if flowers[flower]["train_cnt"] > 0:
                    df1.loc[index, 2] = "training"
                    flowers[flower]["train_cnt"] -= 1
                elif flowers[flower]["val_cnt"] > 0:
                    df1.loc[index, 2] = "validation"
                    flowers[flower]["val_cnt"] -= 1
                    #print(str(index) + " " + flower + " validation")
                else:
                    df1.loc[index, 2] = "testing"
                    #print(str(index) + " " + flower + " testing")

            flowers[flower]["cnt"] += 1

        df1.reset_index(inplace=True, drop=True)
        print(df1)

        csv_out_fname = "lists/generated/daisy_increment/daisy_{}.tsv".format(flowers["daisy"]["total_cnt"])

        df1.to_csv(csv_out_fname, "\t", header=False, index=False)

        # group by flowername (1) and dataset (2) and count occurances
        print(df1.groupby(by=[1, 2])[1].count())

# ----------------------------------------------------------------------------------------------------------------------

# all increment --------------------------------------------------------------------------------------------------------
if False:
    for i in range(0, 135, 5):
        df1 = df.copy()

        flowers = {
            "daisy":        {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "dandelion":    {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "roses":        {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "sunflowers":   {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
            "tulips":       {"cnt": 0, "total_cnt": 0, "train_cnt": 0, "val_cnt": 0},
        }

        # split
        # 80% training
        # 20% validation
        for key in flowers:
            flowers[key]["total_cnt"] = 20+i
            flowers[key]["train_cnt"] = int((flowers[key]["total_cnt"] / 100) * 80)
            flowers[key]["val_cnt"] = int((flowers[key]["total_cnt"] / 100) * 20)

        total_cnt = 400+20+i  # including test with 400 files

        for index, row in df1.iterrows():
            flower = row[1]
            if flowers[flower]["cnt"] >= total_cnt:
                df1.drop([index], inplace=True)
            else:
                if flowers[flower]["train_cnt"] > 0:
                    df1.loc[index, 2] = "training"
                    flowers[flower]["train_cnt"] -= 1
                elif flowers[flower]["val_cnt"] > 0:
                    df1.loc[index, 2] = "validation"
                    flowers[flower]["val_cnt"] -= 1
                else:
                    df1.loc[index, 2] = "testing"

            flowers[flower]["cnt"] += 1

        df1.reset_index(inplace=True, drop=True)
        print(df1)

        csv_out_fname = "lists/generated/all_increment/all_increment_{}.tsv".format(flowers["daisy"]["total_cnt"])

        df1.to_csv(csv_out_fname, "\t", header=False, index=False)

        # group by flowername (1) and dataset (2) and count occurances
        print(df1.groupby(by=[1, 2])[1].count())

# ----------------------------------------------------------------------------------------------------------------------

# all increment random -------------------------------------------------------------------------------------------------
if True:
    for run in range(0, 3):
        flowers = {
            "daisy": {"cnt": 0},
            "dandelion": {"cnt": 0},
            "roses": {"cnt": 0},
            "sunflowers": {"cnt": 0},
            "tulips": {"cnt": 0},
        }

        df_new = pd.DataFrame()

        test_pics = 400

        classes = ["daisy", "dandelion", "roses", "sunflowers", "tulips"]
        pictcnt_each_class = 150
        pictcnt_each_add = 5

        for i in range(0, pictcnt_each_class*len(classes)):
            if len(classes) == 0:
                break

            classToAdd = secrets.choice(classes)

            while flowers[classToAdd]["cnt"] >= pictcnt_each_class+test_pics:
                classes.remove(classToAdd)

                if len(classes) == 0:
                    break

                classToAdd = secrets.choice(classes)

            # split: train 60; val 40;
            # for 5 picts -> 3 1 1
            train_cnt = int((pictcnt_each_add / 100) * 80)
            val_cnt = int((pictcnt_each_add / 100) * 20)

            print("adding pictures to class {} train: {} val: {} test: {}".format(classToAdd, train_cnt, val_cnt, pictcnt_each_add - train_cnt - val_cnt))
            print("left classes {}".format(classes))

            df_select = df.loc[df[1] == classToAdd]
            cnt = pictcnt_each_add
            offset = flowers[classToAdd]["cnt"]
            for index, row in df_select.iterrows():
                if offset > 0:
                    offset -= 1
                else:
                    if flowers[classToAdd]["cnt"] < pictcnt_each_class + test_pics and cnt > 0:
                        if train_cnt > 0:
                            df_new = df_new.append({0: row[0], 1: row[1], 2: "training"}, ignore_index=True)
                            train_cnt -= 1
                        elif val_cnt > 0:
                            df_new = df_new.append({0: row[0], 1: row[1], 2: "validation"}, ignore_index=True)
                            val_cnt -= 1
                        else:
                            assert False

                        cnt -= 1
                        flowers[classToAdd]["cnt"] += 1
                    else:
                        if flowers[classToAdd]["cnt"] < test_pics + pictcnt_each_add:
                            df_new = df_new.append({0: row[0], 1: row[1], 2: "testing"}, ignore_index=True)
                            flowers[classToAdd]["cnt"] += 1
                        else:
                            break


            csv_out_fname = "lists/generated/random_increment/{}/random_increment_{}.tsv".format(run, i)

            if not os.path.exists("lists/generated/random_increment/{}/".format(run)):
                os.makedirs("lists/generated/random_increment/{}/".format(run))

            df_new.to_csv(csv_out_fname, "\t", header=False, index=False)
            print(df_new.groupby(by=[1, 2])[1].count())

# ----------------------------------------------------------------------------------------------------------------------
