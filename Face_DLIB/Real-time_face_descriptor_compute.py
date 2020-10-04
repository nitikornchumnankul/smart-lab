import dlib        
import cv2          
import time

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_reco_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class Face_Descriptor:
    def __init__(self):
        self.frame_time = 0
        self.frame_start_time = 0
        self.fps = 0

    def update_fps(self):
        now = time.time()
        self.frame_time = now - self.frame_start_time
        self.fps = 1.0 / self.frame_time
        self.frame_start_time = now

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 480)
        self.process(cap)
        cap.release()
        cv2.destroyAllWindows()

    def process(self, stream):
        while stream.isOpened():
            flag, img_rd = stream.read()
            k = cv2.waitKey(1)
            frame = cap.read()

            #faces = face_detector(img_rd, 0)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            font = cv2.FONT_HERSHEY_SIMPLEX

            # 检测到人脸
            if len(faces) != 0:
                for face in faces:
                    face_shape = face_detector(img_rd, face)
                    face_desc = face_reco_model.compute_face_descriptor(img_rd, face_shape)

            # 添加说明
            cv2.putText(img_rd, "Face Descriptor", (20, 40), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(img_rd, "FPS:   " + str(self.fps.__round__(2)), (20, 100), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(img_rd, "Faces: " + str(len(faces)), (20, 140), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(img_rd, "S: Save current face", (20, 400), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(img_rd, "Q: Quit", (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

            # 按下 'q' 键退出
            if k == ord('q'):
                break

            self.update_fps()

            cv2.namedWindow("camera", 1)
            cv2.imshow("camera", img_rd)


def main():
    Face_Descriptor_con = Face_Descriptor()
    Face_Descriptor_con.run()


if __name__ == '__main__':
    main()