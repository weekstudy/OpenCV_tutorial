import cv2
import time


class CapVideo(object):
    def __init__(self, out_fps=24, size=(640, 480)):
        self.fps = out_fps
        self.size = size

    def cap_video(self, filename):
        # 输出文件的帧率
        out_fps = self.fps
        # 表示打开默认的相机
        cap = cv2.VideoCapture(0)
        # 获取捕获图像的分辨率
        size = self.size
        # 编码格式
        fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
        # 设置视频的编码,分辨率和帧率
        video = cv2.VideoWriter(filename, fourcc, out_fps, size)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame', frame)
                video.write(frame)
                # 这个函数接收一个整型值，如果这个值是零，那么函数不会有返回值，
                # 如果delay大于0，那么超过delayms后，如果没有按键，那么会返回 - 1，如果按键那么会返回键盘值
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            else:
                break

        video.release()
        cap.release()
        cv2.destroyAllWindows()


class CapFrame(object):
    def __init__(self, filename, fps=24):
        self.filename = filename
        self.fps = fps

    def cap_frame(self):
        import os
        # 要提取视频
        filename = self.filename
        timestamp = 0
        # 提取视频的频率，
        fps = self.fps
        # 输出图片到当前目录images文件夹下
        out_put_dir = 'images/'
        if not os.path.exists(out_put_dir):
            # 如果文件目录不存在则创建目录
            os.makedirs(out_put_dir)
        cap = cv2.VideoCapture(filename)
        while True:
            timestamp += 1
            res, image = cap.read()
            if not res:
                print('not res , not image')
                break
            # 每24帧提取一张
            if timestamp % fps == 0:
                cv2.imwrite(out_put_dir + str(timestamp) + '.jpg', image)
                print(out_put_dir + str(timestamp) + '.jpg')
        print('图片提取结束')
        cap.release()


if __name__=="__main__":
    video=CapVideo()
    video.cap_video('test_video.avi')
    frame=CapFrame('test_video.avi')
    frame.cap_frame()
