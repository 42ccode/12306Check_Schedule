"""
# 1.数据来源分析
#     1.获取车次信息
#         通过浏览器抓包分析,这些车次信息,在哪个url里面
#         抓包分析--> 开发者工具进行抓包
        1.打开开发者工具 选择network
        2.点击网页查询按钮-->会直接返回查询数据结果
请求:https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2024-07-02&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT
可以得到相关车次信息内容   更换其他地点进行更新!
# 2.代码实现
    1.发送请求,模拟浏览器对url地址发送请求
    2.获取数据,获取服务器返回的响应数据
    3.解析数据,提取我们想要车次信息
    4.查询功能实现,根据输入不同城市,以及时间点 获取不同的车次信息
"""

# 导入数据请求模块
import requests
# 导入 美化表格
import prettytable as pt
import json

# 导入json模块
"""
    实现查询功能:
    输入出发城市
    输入到达城市
    输入出发时间
城市名字:字母
"""
f = open('city.json', encoding='utf-8')
# f.read()返回字符串数据类型 把字符串转成json字典数据 --> 根据键值对取值
json_data = json.loads(f.read())
# 输入内容
from_city = input('请输入你要出发的城市:')
to_city = input('请输入你要到达的城市:')
date = input('请输入出发时间:')


# 确定请求链接 Request URL:GET METHOD    将上面的from_city to_city date 替换进下面的url链接中  请输入出发时间2024-07-03时间格式
url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_city]}&leftTicketDTO.to_station={json_data[to_city]}&purpose_codes=ADULT'
# 添加请求头信息 headers  添加cookie 和 请求头 User-Agent
headers = {
    'Cookie': '__your_cookie__',    #需修改
    'User-Agent': '__User-Agent__', #需修改
}
# 发送请求  抓取选择get  添加headers请求头
response = requests.get(url=url, headers=headers)
# <Response [200]>表示请求成功了
print(response)
if str(response) == "<Response [200]>":
    print("链接正常")
else:
    print("如获取失败,请检查网络状态码")

# 2.获取数据,获取服务器响应数据
# 常见报错:JSONDecodeError: Expecting value: line 1 column 1 (char 0)
# 解决方法:
#     1.获取response.text,看数据返回情况
#         -发现自己获取的数据,和开发者工具preview中不同 因为有反爬 (得不到数据\得到的数据不是想要的)
#             没有伪装,加上headers
# 2.json()  获取响应json字典数据  完整的{}
# text()   获取响应文本数据 字符串数据  通常是网页源代码
# 字典取值 --> 键值对取值,根据冒号左边的内容key 提取value

# 实例化一个对象
tb = pt.PrettyTable()  # 注意包名大小写
# 输出添加字段名
tb.field_names = [
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '所耗时间',
    '特等座',
    '一等',
    '二等',
    '软卧',
    '硬卧',
    '硬座',
    '无座',
    '软座'
]
page = 0
# for循环遍历,把列表里面元素一个一个提取出来
for i in response.json()['data']['result']:
    # 先用split分隔,在用列表取值:根据索引位置
    index = i.split('|')  # 会返回一个列表
    num = index[3]  # 车次信息
    start_time = index[8]  # 出发时间
    end_time = index[9]  # 到达时间
    use_time = index[10]  # 所耗费时间
    topGrade = index[32]  # 特等座
    first_class = index[31]  # 一等
    second_class = index[30]  # 二等
    hard_sleeper = index[28]  # 硬卧
    hard_seat = index[29]  # 硬座
    no_seat = index[26]  # 无座
    soft_seat = index[25]
    soft_sleeper = index[23]  # 软卧
    dit = {
        '车次': num,
        '出发时间': start_time,
        '到达时间': end_time,
        '所耗时间': use_time,
        '特等座': topGrade,
        '一等': first_class,
        '二等': second_class,
        '软卧': soft_sleeper,
        '硬卧': hard_sleeper,
        '硬座': hard_seat,
        '无座': no_seat,
        '软座': soft_seat,
    }
    # 添加每行输出内容
    tb.add_row(
        [page, num, start_time, end_time, use_time, topGrade, first_class, second_class, soft_sleeper, hard_sleeper,
         hard_seat, no_seat, soft_seat])
    page += 1
print(tb)

# a = 0
# 方便提取数据 坐标位置
# for j in index:
#     print(j, a, sep="--") #用来查看下标的索引号
#     a += 1
# break
