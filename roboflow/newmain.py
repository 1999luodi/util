import os

import roboflow
import json
import count_seeds

def display_result(imgpath):
    rf = roboflow.Roboflow(api_key="kbkS9eIMbBunFah99BtY")

    project = rf.workspace().project("soybean-seeds")
    model = project.version("1").model

    # optionally, change the confidence and overlap thresholds
    # values are percentages
    model.confidence = 50
    model.overlap = 25

    # predict on a local image
    prediction = model.predict(imgpath)



    # Plot the prediction in an interactive environment
    prediction.plot()

    # Convert predictions to JSON
    txt=prediction.json()
    # path="prediction2.json"
    # with open(path,"w",encoding="utf-8") as outfile:
    #     json.dump(txt,outfile,ensure_ascii=False,indent=4)
    count=count_seeds.count_seeds_byfile(txt)
    return count

if __name__ == "__main__":
    floder_path="./huandou"
    floder_list=os.listdir(floder_path)
    all_count=0
    for item in floder_list:
        item_path=floder_path+"/"+item
        result = display_result(item_path)
        all_count+=result
    print(f"all seed are {all_count} ")