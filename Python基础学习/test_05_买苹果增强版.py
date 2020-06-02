# 收银员输入苹果价格，单位元/斤
# 收银员输入用户购买的重量，单位斤
# 计算且输出付款金额
price_str = input("请输入苹果的单价")
weight_str = input("请输入苹果的重量")
# 注意，两个字符串不能用乘法。将价格和重量转换成小数
price = float(price_str)
weight = float(weight_str)
moeny = price*weight
print(moeny)