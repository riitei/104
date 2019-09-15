from os.path import dirname, join
import json


class Access_job_file:
    def __init__(self):
        project_root = dirname(dirname(__file__))
        # 設定專案讀寫檔案路徑
        self._path = join(project_root, '104', 'job_data')

    # 查詢是否投遞公司職務 url
    def search_job_list(self, search_job_url):
        # 初始沒找到檔案資料
        file_path = join(self._path, "job_url.list")

        try:
        # read file
            try:
                file = open(file_path, "r")
                data = file.read()
                file.close()
            except:
                # 沒檔案初始化
                file = open(file_path, "w")
                file.write("__init__")
                file.close()
                return False
            # str to list
            list = data.split(",\n")
            list.index(search_job_url)
            print("有資料")
            return True
        except:

            # 沒資料
            # file = open(file_path, 'a')
            # file.write(",\n%s" % search_job_url)
            # file.close()
            print("沒資料")
            return False



    #         search_job_name input 104 url
    # 紀錄投遞履歷url
    def job_list_result(self, job_url):
        file_path = join(self._path, "job_url.list")
        file = open(file_path, 'a')
        file.write(",\n%s" % job_url)
        file.close()

    # 紀錄104職務內容 dict
    def job_log_write_dict(self, file_name, data):
        file_path = join(self._path, file_name + ".json")
        file = open(file_path, 'w')
        file.write(json.dumps(data))
        file.close()


    def job_log_read_dict(self, file_name):
        file_path = join(self._path, file_name + ".json")
        try:
            file = open(file_path, 'r')
            data = file.read()
            file.close()
            return json.loads(data)
        except:
            file = open(file_path, 'w')
            data = {}
            file.close()
            return data


# if __name__ == "__main__":
#     reslut = Access_job_file().search_job_list("yanya")
