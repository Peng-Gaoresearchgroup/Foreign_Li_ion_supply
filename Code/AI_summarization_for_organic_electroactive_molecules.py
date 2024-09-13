import time

import DrissionPage.errors
from loguru import logger
from DrissionPage import ChromiumPage, ChromiumOptions
import requests
import os


def main():
    proxies = {'https': 'http://127.0.0.1:7890'}
    try:
        requests.get('https://www.google.com', proxies=proxies, timeout=1)
        proxy = '127.0.0.1:7890'
    except requests.RequestException:
        proxy = None

    old_pdf_files = set()
    if os.path.exists('demo.txt'):
        with open('demo.txt', encoding='utf-8') as f:
            for text in f.read().strip().split('\n'):
                old_pdf_file = text.split('---')[0]
                old_pdf_files.add(old_pdf_file)

    co = ChromiumOptions()
    co.set_local_port(23411)
    co.set_proxy(proxy)
    cp = ChromiumPage(co)
    cp.get('https://chatgpt.com/')
    if cp.ele('登录', timeout=2):
        raise '没有登录chatgpt，无法使用，请在浏览器上登录后重新启动'
    pdf_files = os.listdir('py2')
    pdf_files.sort(key=lambda x: int(x.split('.')[0]))
    for pdf_file in pdf_files:
        if pdf_file in old_pdf_files:
            continue
        pdf_abs_path = os.getcwd() + os.sep + 'py2' + os.sep + pdf_file
        # 读取文件判断大小
        with open(pdf_abs_path, 'rb') as f:
            file_size = len(f.read())
        if file_size < 3000:
            with open('demo.txt', 'a', encoding='utf-8') as f:
                f.write(f'{pdf_file}----非正常文件\n')
        else:
            while True:
                logger.info(f'正在处理：{pdf_file}')
                # 切换到gpt4
                cp.get('https://chatgpt.com/?model=gpt-4o')
                try:
                    cp.ele('tag:input').input(pdf_abs_path)
                except DrissionPage.errors.ElementLostError:
                    time.sleep(5)
                    cp.ele('tag:input').input(pdf_abs_path)
                text = """
                “假设你是有机电化学领域的专家，请帮我总结一下这篇文献里主要研究的分子以及发生的反应过程，用英文按以下格式回复（被【】圈起来的是变量，需要你从pdf中提取，如果提取不到的留空处理，不要回复额外内容）：
                1.[化合物A][CAS号]在[xxx]条件下发生反应，产物为[化合物B][CAS号]”
                """
                cp.ele('#prompt-textarea').input(text)
                while True:
                    if 'disabled' in cp.ele('@data-testid=send-button').attrs:
                        time.sleep(1)
                        continue
                    cp.ele('@data-testid=send-button').click()
                    break
                if '无法上传' in cp.html:
                    continue
                reply_text = cp.ele('.markdown prose w-full break-words dark:prose-invert light', timeout=50).text
                with open('demo.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{pdf_file}----{reply_text}\n')

                break


if __name__ == '__main__':
    main()
