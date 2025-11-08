import uuid
import requests
import time
import os
from typing import Dict, Any
import threading  # 新增导入 threading 模块

class HTTPRequest:
    # 默认配置
    default_options = {
        'headers': {
            'Content-Type': 'application/json;charset=UTF-8',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
        },
        'timeout': 10,  # 超时时间（秒）
    }

    @staticmethod
    def _merge_headers(default_headers: Dict[str, str], custom_headers: Dict[str, str]) -> Dict[str, str]:
        """合并默认头部和自定义头部"""
        return {**default_headers, **custom_headers}

    @staticmethod
    def _build_url_params(params: Dict[str, Any]) -> str:
        """将字典格式的参数转换为查询字符串"""
        return '&'.join([f"{k}={v}" for k, v in params.items()])

    @staticmethod
    def post(url: str, data: Dict[str, Any], options: Dict[str, Any] = {},) -> Dict[str, Any]:
        """发送 POST 请求"""
        try:    
            request_url = url

            final_options = {
                'method': 'POST',
                'url': request_url,
                'headers': HTTPRequest._merge_headers(HTTPRequest.default_options['headers'], options.get('headers', {})),
                'json': data,
                'timeout': options.get('timeout', HTTPRequest.default_options['timeout']),
            }
            response = requests.request(**final_options)
            response.raise_for_status()  # 检查响应状态码
            return response.json()  # 假设返回的是 JSON 格式
        except requests.exceptions.RequestException as e:
            print(f"HTTP POST request failed: {e}")
            raise

    @staticmethod
    def get(url: str, params: Dict[str, Any] = {}, options: Dict[str, Any] = {}) -> Dict[str, Any]:
        """发送 GET 请求"""
        try:
            query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
            request_url = f"{url}?{query_string}" if query_string else url

            final_options = {
                'method': 'GET',
                'url': request_url,
                'headers': HTTPRequest._merge_headers(HTTPRequest.default_options['headers'], options.get('headers', {})),
                'timeout': options.get('timeout', HTTPRequest.default_options['timeout']),
            }
            response = requests.request(**final_options)
            response.raise_for_status()  # 检查响应状态码
            return response.json()  # 假设返回的是 JSON 格式
        except requests.exceptions.RequestException as e:
            print(f"HTTP GET request failed: {e}")
            raise

    @staticmethod
    def login_count_post_request():
        """示例：使用 post 方法发送请求"""

        url = 'https://api.yesapi.net/api/SVIP/Szwyzzz888_MyApi/AUpdateMir2logincount'
        mac = uuid.getnode()  # 返回整型 MAC 地址
        mac_address = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0, 8 * 6, 8)][::-1])

        postData = {
            "app_key": "C9D0523F019B3D49CF0D62F5CDCDF60F",
            "username": mac_address,  # 使用格式化后的 MAC 地址
            "logintime": str(int(time.time())),  # 当前时间的10位时间戳
            "loginip": requests.get('https://ipecho.net/plain').text.strip(),  # 获取本机外网IP
            "info": ', '.join([f for f in os.listdir('Data') if f.endswith('.itm')]) if os.path.exists('Data') else "",  # 拼接Data目录下的.itm文件名
            "sourceType": "1",
            "yesapi_allow_origin": "1"
        }

        try:
            response = HTTPRequest.post(url, postData)
        except Exception as e:
            print("Error:", e)


# 新增方法：在新线程中执行 login_count_post_request
def run_login_count_in_thread():
    thread = threading.Thread(target=HTTPRequest.login_count_post_request)
    thread.start()