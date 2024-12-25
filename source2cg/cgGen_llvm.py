import argparse
import os
import subprocess
import shutil
import glob


def move_and_rename_file(path1, path2):
    try:
        # Check if path1 is a valid file
        if not os.path.isfile(path1):
            print(f"Error: {path1} is not a valid file path!")
            return

        # Check if the parent directory of the destination path exists
        target_dir = os.path.dirname(path2)
        if not os.path.exists(target_dir):
            print(f"Error: The destination directory {target_dir} does not exist!")
            return
        
        # Move and rename the file
        shutil.move(path1, path2)
        print(f"File has been moved from {path1} and renamed to {path2}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def parse_source_code(source_file_path):
    """Reads the source code file and returns its lines."""
    with open(source_file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)  # 删除文件

def rename_file(old_file_name,new_file_name):
    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)  # 重命名文件

def main():
    # 创建解析器
    parser = argparse.ArgumentParser(description="Read file_name and function_name from command-line arguments.")
    
    # 添加两个必需的参数 file_name 和 function_name
    parser.add_argument('file_name', type=str, help="The name of the file")

    # 解析参数
    args = parser.parse_args()

    file_name = args.file_name
    
    input_folder = "input"

    file_path  = os.path.join(input_folder, file_name)

    # 输出参数
    print("File name:", args.file_name)

    pure_file_name = file_name.split('.', 1)[0]

    dot_file_path = f'{pure_file_name}.ll.callgraph.dot'
    ir_file_path = f"{pure_file_name}.ll"

    # 输出文件夹
    output_folder = "output"

    # 创建 output 文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 构建文件路径
    final_file_path = os.path.join(output_folder, f".{file_name.split('.', 1)[0]}.dot")
    png_file_path = os.path.join(output_folder, f"{file_name.split('.', 1)[0]}.png")


    # 使用 subprocess 运行 clang 命令
    command_1 = ["clang", "-S", "-emit-llvm", file_path, "-o", ir_file_path ]

    command_2 = ["opt","-dot-callgraph", "-disable-output","-enable-new-pm=0",ir_file_path ]

    # 执行命令
    try:
        subprocess.run(command_1, check=True)
        print(f"successfully generated IR: {ir_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"fail in generating IR: {e}")
    

    # 调用命令
    try:
        subprocess.run(command_2, check=True)
        print(f"successfully generated dot: {dot_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"fail in generating dot: {e}")

    move_and_rename_file(dot_file_path,final_file_path)


    # 构造命令
    command_3 = ["dot", "-Tpng", f"-o{png_file_path}", final_file_path]

    try:
        subprocess.run(command_3, check=True)
        print(f"successfully generated png: {png_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"fail in generating png: {e}")
    
    # 获取当前目录下所有 .dot 文件
    dot_files = glob.glob(".*.dot")
    

    # 删除每个 .dot 文件
    for dot_file in dot_files:
        os.remove(dot_file)
    
      # 获取当前目录下所有 .dot 文件
    ll_files = glob.glob("*.ll")
    

    # 删除每个 .dot 文件
    for ll_file in ll_files:
        os.remove(ll_file)

    

if __name__ == "__main__":
         main()

