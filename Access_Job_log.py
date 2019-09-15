from os.path import dirname, join


class Access_Job_log:
    def __init__(self):
        project_root = dirname(dirname(__file__))
        # 設定專案讀寫檔案路徑
        self._path = join(project_root, '104', 'job_data')

    def search_job_list(self, search_job_name):
        # 初始沒找到檔案資料
        file_path = join(self._path, "job_url.list")
        print(file_path)

        try:
            # read file
            try:
                file = open(file_path, "r")
                data = file.read()
                file.close()
            except:
                # 沒檔案初始化
                file = open(file_path, "w")
                file.write(search_job_name)
                file.close()
                return False
            # str to list
            list = data.split(",\n")
            list.index(search_job_name)
            print("yes")
            # 有資料
            return True
        except:
            # 沒資料
            file = open(file_path, 'a')
            file.write(",\n%s" % search_job_name)
            file.close()
            return False
            print("沒資料")


if __name__ == "__main__":
    reslut = Access_Job_log().search_job_list("yanya")
    print(reslut)
