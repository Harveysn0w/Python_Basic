#! /usr/local/bin/python3

import cards_tools
while True:      # 无限循环，由用户主动决定什么时候退出循环

    # TODO（Harvey） 显示功能菜单 ~ 编写完所需代码应该删除TODO

    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作： ")
    print("您选择的操作是【%s】" % action_str)

    # 1，2，3针对名片的操作   0是退出系统   其他则提示内容输入错误，请从新输入
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")

        break
        # 如果在开发程序时，不希望立即编写分支内部的代码，
        # 可以使用pass关键字，表示一个占位符能够表示代码结构正确
        # pass
    else:
        print("您输入的不正确，请重新选择")
