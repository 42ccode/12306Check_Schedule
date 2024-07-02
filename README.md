车次查询程序 README
1. 数据来源分析 (Data Source Analysis)
通过抓包分析，获取12306火车票查询接口的数据。
请求链接格式：https://kyfw.12306.cn/otn/leftTicket/query
2. 代码实现 (Implementation)
使用Python编写，依赖requests库发送HTTP请求，prettytable库美化输出表格。
用户输入：出发城市、到达城市、出发时间。
解析12306返回的JSON数据，提取车次信息并用表格显示。
3. 如何使用 (How to Use)
首先确保安装了Python环境和所需库（requests和prettytable）。
运行程序时，根据提示输入城市名称和日期，即可查询相应车次信息。
4. 注意事项 (Notes)
确保网络连接正常，可以访问12306网站。
如果出现获取数据失败，可能需要更新请求头或处理反爬虫机制。
5. 示例 (Example)
示例代码运行截图或输出结果。
6. 作者及联系方式 (Author and Contact)
作者：42ccode
联系方式：42ccode@gmail.com
7. 目前暂时只支持以下城市: (待后续更新···)
{
  "北京": "BJP",
  "上海": "SHH",
  "天津": "TJP",
  "重庆": "CQW",
  "武汉": "WHN",
  "昆明": "KMM",
  "深圳": "SZQ",
  "郑州": "ZZF"
}
8.Train Schedule Query Program README
1. Data Source Analysis
Fetching data from the 12306 train ticket query API through packet capture analysis.
Request URL format: https://kyfw.12306.cn/otn/leftTicket/query
2. Implementation
Developed in Python using the requests library for sending HTTP requests and prettytable for displaying formatted tables.
User inputs: Departure city, destination city, and travel date.
Parsing JSON responses from 12306 to extract train schedule information and displaying it in a table format.
3. How to Use
Ensure Python environment is set up with necessary libraries (requests and prettytable).
Run the program and follow the prompts to enter city names and dates to query train schedules.
4. Notes
Ensure stable internet connection to access the 12306 website.
If data retrieval fails, consider updating request headers or handling anti-scraping mechanisms.
5. Example
Include screenshots or output samples of the program in action.
6. Author and Contact Information
Author: 42ccode
Contact: 42ccode@gmail.com
7. Currently only the following cities are supported: (to be updated later...){
  "北京": "BJP",
  "上海": "SHH",
  "天津": "TJP",
  "重庆": "CQW",
  "武汉": "WHN",
  "昆明": "KMM",
  "深圳": "SZQ",
  "郑州": "ZZF"
}