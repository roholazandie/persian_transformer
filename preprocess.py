from tqdm import tqdm
import os
import json
import random

def convert_to_txt_files(json_path, out_path):
    for root, dirs, files in os.walk(json_path):
        for file in tqdm(files):
            file_path = os.path.join(root, file)
            with open(file_path) as fr:
                text = fr.read()
                json_text = text.replace("}", "},")
                json_text = json_text[::-1].replace(",", "", 1)[::-1]
                json_text = "[" + json_text + "]"
                docs = json.loads(json_text)
                docs = [doc['text'].replace("\n\n", " ") for doc in docs]
                #docs = " ".join(docs)
                file = file + str(random.randint(1,10000)) #todo need a better solution, duplicate?
                out_file_path = os.path.join(out_path, file)
                open(out_file_path, 'w').writelines(docs)


def divide_to_train_eval(txt_paths, out_dir):
    train_writer = open(os.path.join(out_dir, "train.txt"), 'w')
    eval_writer = open(os.path.join(out_dir, "eval.txt"), 'w')

    for root, dirs, files in os.walk(txt_paths):
        num_files = len(files)
        for i, file in enumerate(files):
            file_path = os.path.join(root, file)
            lines = open(file_path).readlines()
            if i < int(0.8 * num_files):
                train_writer.writelines(lines)
            else:
                eval_writer.writelines(lines)


if __name__ == "__main__":
    json_path = "clean_wiki_text_json/"
    out_path = "clean_wiki_text_txt"
    train_eval_path = "data/"
    #convert_to_txt_files(json_path, out_path)
    divide_to_train_eval(out_path, train_eval_path)