import argparse
import sys

def read_file_and_count_chars(filename, output_file=None):
    """
    读取指定文件，统计除换行符以外的字符数，并打印（或写入）文件内容。

    Args:
        filename (str): 要读取的文件路径。
        output_file (str or None): 可选，输出文件路径。如果为 None，则输出到控制台。
    """
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 未找到。请检查文件路径和名称是否正确。", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"错误：无法使用 'utf-8' 编码读取文件 '{filename}'。请确保文件是 UTF-8 格式。", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错：{e}", file=sys.stderr)
        sys.exit(1)

    # 移除每行首尾的空白字符（包括换行符）
    lines = [line.strip() for line in lines]
    content = ''.join(lines)
    char_count = len(content)

    # 准备输出内容
    output_lines = [
        f"文件 '{filename}' 共有 {char_count} 个字符（不含换行符）。",
        "文件内容如下：",
        content
    ]
    output_text = "\n".join(output_lines)

    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as out:
                out.write(output_text)
            print(f"结果已写入文件：{output_file}")
        except Exception as e:
            print(f"写入输出文件时出错：{e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("\n" + output_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="一个用于统计文件字符数并显示内容的命令行工具。",
        epilog="示例用法: python your_script_name.py C:/path/to/file.txt -o output.txt"
    )
    parser.add_argument(
        'filename',
        type=str,
        help="要处理的文件的完整路径和名称"
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        help="可选：指定输出文件路径（若提供，则结果写入该文件而非打印到控制台）"
    )

    args = parser.parse_args()
    read_file_and_count_chars(args.filename, output_file=args.output)