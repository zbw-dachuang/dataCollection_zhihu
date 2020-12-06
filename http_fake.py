# _*_ coding:utf-8 _*_


# 这部分用于请求头的伪装

# UA 伪装
def UA_fake():
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'
    }
    return header
# Cookie
def Cookie():
    cookie = {
        'cookie': 'KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1606725786|1606725782; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1606702456; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1606699037,1606700119,1606701998,1606702456; JOID=Wl0XAE_VKYoQhkm-N97oWs8Cjy0su3zPU-ww40HtRcJg4Hz0YDKfMUSHQ7gxg7Y33ZwWwo97EdC9SVFL7GyV6-o=; SESSIONID=cRDDftZw4aOqa9GPKQmmkM2yTiAQAH1Yt3jnp5W1iPG; osd=VFkRBELbLYwUi0e6MdrlVMsEiyAiv3rLXuI05UXgS8Zm5HH6ZDSbPEqDRbw8jbIx2ZEYxol_HN65T1VG4miT7-c=; tst=r; _xsrf=971e53cb-5eb3-4524-9aec-6eb7eb935b74; __utma=51854390.1952247788.1606228945.1606228945.1606228945.1; __utmv=51854390.100--|2=registration_date=20181230=1^3=entry_date=20181230=1; __utmz=51854390.1606228945.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/381011221; q_c1=d22a9c41144e422bb6d6cdc0e5bd2b0d|1605000760000|1580380931000; z_c0="2|1:0|10:1598841166|4:z_c0|92:Mi4xc1ZQRURRQUFBQUFBVUtLd3hndDlFQ1lBQUFCZ0FsVk5UcTg1WUFBQUJFTF95Yk5sTng3ZUt1el9XUVVEbWQycjhR|12062d89526c26b0c05765a677e3923a9a55279b981a32c78f2c0d663d1fdd03"; _zap=c4c1c013-e8b4-4504-8a2a-b515d4402743; d_c0="AFCisMYLfRCPTq8pg5vEJR9vG5zFdijtSzA=|1576049601'
    }
    return cookie