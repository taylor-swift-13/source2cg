
import os
import subprocess
import shutil

# 指定 input 文件夹的路径
input_folder = 'input'
doxyfile_path = os.path.join(input_folder, 'Doxyfile')
html_output_dir = os.path.join(input_folder, 'html')
latex_output_dir = os.path.join(input_folder, 'latex')
run_doxyfile = './Doxyfile'



def modify_doxyfile():
    # 检查 Doxyfile 是否存在
    if not os.path.exists(doxyfile_path):
        print(f"Error: The file '{doxyfile_path}' does not exist.")
        return

    try:
        # 读取 Doxyfile 内容
        with open(doxyfile_path, 'r') as file:
            lines = file.readlines()
        
        # 定义要修改的选项
        modifications = {
            'HAVE_DOT': 'YES',  # 启用 Graphviz DOT 图形支持
            'CALL_GRAPH': 'YES',  # 启用生成函数调用图
            'EXTRACT_ALL': 'YES',  # 提取所有成员（包括私有成员）
            'REFERENCES_RELATION': 'YES'  # 启用生成引用关系图
        }

        # 修改 Doxyfile 中的相关选项
        for i, line in enumerate(lines):
            for key, value in modifications.items():
                if line.startswith(key):
                    lines[i] = f"{key} = {value}\n"

        # 将修改后的内容写回 Doxyfile
        with open(doxyfile_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Successfully updated the Doxyfile: {doxyfile_path}")

    except Exception as e:
        print(f"Error modifying Doxyfile: {e}")



def gen_doxyfile():
    # 检查 input 文件夹是否存在
    if not os.path.exists(input_folder):
        print(f"Error: The directory '{input_folder}' does not exist.")
        return
    
    # 运行 doxygen -g 命令
    try:
        # 执行 doxygen -g 命令，生成 Doxygen 配置文件 (Doxyfile)
        subprocess.run(['doxygen', '-g'], cwd = input_folder ,check=True)
        print("Doxygen configuration file (Doxyfile) generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running doxygen: {e}")
        return
    except FileNotFoundError:
        print("Error: Doxygen is not installed or not found in system path.")
        return
    



def run_doxygen():
    
    # 执行 doxygen ./Doxyfile 命令
    try:
        # 执行命令
        result = subprocess.run(['doxygen', run_doxyfile], cwd = input_folder,check=True, text=True, capture_output=True)
        
        # 打印命令输出（标准输出和错误输出）
        print("Doxygen executed successfully.")
        print("Output:")
        print(result.stdout)
        print("Error:")
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error while running doxygen: {e}")
        print(f"Output: {e.output}")
        print(f"Error Output: {e.stderr}")
    except FileNotFoundError:
        print("Error: Doxygen is not installed or not found in the system path.")
        return


def delete_file(file_path):
    """ 删除单个文件 """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Successfully deleted the file: {file_path}")
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")


def delete_directory(directory_path):
    """ 删除目录及其内容 """
    try:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print(f"Successfully deleted the directory: {directory_path}")
        else:
            print(f"Directory not found: {directory_path}")
    except Exception as e:
        print(f"Error deleting directory {directory_path}: {e}")


def delete_doxygen():
    """ 删除 Doxyfile 和 Doxygen 生成的 HTML、LaTeX 文件 """
    # 删除 Doxyfile
    delete_file(doxyfile_path)

    # 删除 HTML 输出目录
    delete_directory(html_output_dir)

    # 删除 LaTeX 输出目录
    delete_directory(latex_output_dir)

def gen_doxygen():
    if not os.path.exists(doxyfile_path):
        print("Doxyfile does not exist, generating new one.")
        gen_doxyfile()

    modify_doxyfile()
    run_doxygen()


# Doxyfile 配置文件路径

def main():
    
    gen_doxygen()
    # delete_doxygen()

if __name__ == "__main__":
    main()