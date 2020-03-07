#!/usr/bin/python
# -*- coding:utf-8 -*-

# 自定义分页实现（模块化）
# from django.utils.safestring import mark_safe
# https://www.cnblogs.com/luotianshuai/p/5377233.html


class Pager(object):
    def __init__(self, current_page):
        self.current_page = int(current_page)
    
    #把方法伪造成属性-->  调用方法的时候就不需要加括号
    @property
    def start(self):
        return (self.current_page - 1) * 10

    @property
    def end(self):
        return self.current_page * 10

    def page_str(self, all_item, base_url):
        # divmod(500,10)，他会的到一个元组，第一个值是值，第二个值是余数
        all_page, div = divmod(all_item, 10)

        if div > 0:  # 如果有余数,在整页上+1
            all_page += 1

        pager_list = []

        #默认可以看到的页码11个
        if all_page <= 11:
            start = 1
            end = all_page
        else:
            if self.current_page <= 6:
                start = 1
                end = 11 + 1
            else:
                start = self.current_page - 5
                end = self.current_page + 6
                if self.current_page + 6 > all_page:
                    start = all_page - 10
                    end = all_page + 1

        #把页面动态起来传入起始和结束
        for i in range(start, end):

            #判断是否为当前页
            if i == self.current_page:
                temp = '<a style="color:red;font-size:26px;padding: 5px" href="%s?page=%d">%d</a>' % (
                    base_url, i, i)
            else:
                temp = '<a style="padding: 5px" href="%s?page=%d">%d</a>' % (
                    base_url, i, i)

            # 把标签拼接然后返回给前端
            pager_list.append(temp)

        #上一页
        if self.current_page > 1:
            pre_page = '<a href="%s?page=%d">上一页</a>' % (
                base_url, self.current_page - 1)
        else:
            # javascript:void(0) 什么都不干
            pre_page = '<a href="javascript:void(0);">上一页</a>'
        #下一页
        if self.current_page >= all_page:
            next_page = '<a href="javascript:void(0);">下一页</a>'
        else:
            next_page = '<a href="%s?page=%d">下一页</a>' % (
                base_url, self.current_page + 1)

        pager_list.insert(0, pre_page)
        pager_list.append(next_page)
        return pager_list
        # return mark_safe("".join(pager_list))


if __name__=='__main__':
    current_page = 1 # request.GET.get('page', 1)
    page_obj = Pager(current_page)
    #把方法改造成属性,下面调用方法的时候就不需要加括号了
    # result = models.UserList.objects.all()[page_obj.start:page_obj.end]
    # all_item = models.UserList.objects.all().count()
    # pager_str = page_obj.page_str(all_item,'/user_list/')