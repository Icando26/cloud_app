import yaml, os


def ret_yaml_data(file_name):
    file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name + ".yml"
    print(file_path)
    with open(file_path, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)




# data_a = {'a': {'name': 'lili', 'pwd': '456', 'sex': '男'}}
# file_path = os.getcwd()+ os.sep + "../Data" + os.sep + "data.yml"
# print(file_path)
# 加载
# with open(file_path, "w") as f:
#     data = yaml.dump(data_a, f, encoding='utf-8', allow_unicode=True)

# 解析
# with open(file_path, "r") as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     items = data.get("Search_Data")
#     print(data)
#
#     for key in items.keys():
#         print(items.get(key))
