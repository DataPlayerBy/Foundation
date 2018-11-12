import itchat
from itchat.content import *
import multiprocessing
import time


# itchat.auto_login(hotReload=True)   # 登录，会弹出一个二维码，手机扫码登录
# itchat.logout()  #退出登录
# itchat.get_contact(update=True)    # 获取消息页面的消息列表
# itchat.get_friends(update=True)   # 获取通讯录页面的好友列表
# itchat.get_chatrooms(update=True)   # 获取通讯录/群聊页面的列表
# itchat.get_mps(update=True)   # 获取通讯录/公众号页面的列表
# itchat.search_friends(name='李倩')  # 查找通讯录中的好友
# itchat.search_chatrooms(name='福利')    # 查找通讯录/群聊页面中的群
# itchat.search_mps(name='玩卡大本营')    # 查找通讯录/公众号页面中的公众号
# itchat.get_head_img(userName='@7aeceb2bcc7892f010d35770752404072c4570cd16a97f158c56b0436d545ec2', picDir='/Users/gaojingbin/Downloads/1.png')  # 获取通讯录中的好友头像，userName通过search_friends()或者get_friends()方法获取

# # 发送文件/图片/消息/视频，toUsername不是用户的昵称或备注，而是一串id，需要通过先查找用户，再获取，文件传输助手的userName为filehelper
# itchat.send(msg='@fil@/Users/gaojingbin/Downloads/tutorial-examples.tar.gz', toUserName='@a185b85863b43ad38ebe2831bec0cb9b')
# itchat.send(msg='@img@/Users/gaojingbin/Downloads/1.jpeg', toUserName='@a185b85863b43ad38ebe2831bec0cb9b')
# itchat.send(msg='@msg@你好呀', toUserName='@a185b85863b43ad38ebe2831bec0cb9b')
# itchat.send(msg='@vid@/Users/gaojingbin/Downloads/1541926366755523.mp4', toUserName='@a185b85863b43ad38ebe2831bec0cb9b')

# itchat.revoke(msgId='5765689692917646548', toUserName='@a185b85863b43ad38ebe2831bec0cb9b')  #撤销消息，msgId可以从发送成功的消息的返回值中获得

# 应用部分
# # 各种消息的获取与自动回复，消息类型，TEXT:文字、表情、视频通话、语音通话、语音输入，MAP:位置，CARD:名片，NOTE:红包、转账，SHARING:分享，PICTURE:图片，RECORDING:语音消息，ATTACHMENT:文件，VIDEO:拍摄、视频，FRIENDS:好友申请
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print('1', msg.type)
    msg.user.send('%s' % msg.type)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    print('2', msg.type)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print('3', msg.type)
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)    # 群聊中@我的情况
def text_reply(msg):
    print('4', msg.type)
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


itchat.auto_login(hotReload=True)
itchat.run()

# 微信多开
# def run_wechat(number):
#     wechat_instance = itchat.new_instance()
#     wechat_instance.auto_login(hotReload=True, statusStorageDir='instance_{}.pkl'.format(number))
#
#     @wechat_instance.msg_register(itchat.content.TEXT)
#     def reply(msg):
#         return msg.text
#
#     wechat_instance.run()
#
#
# pool = multiprocessing.Pool(processes=3)
# for i in range(2):
#     pool.apply_async(run_wechat, (i, ))
#     print('start{}'.format(i))
#     time.sleep(30)
#
# pool.close()
# pool.join()
