from detector import ObjectDetector

detector = ObjectDetector()

print("Choose Mode:")
print("1 → Image")
print("2 → Video")
print("3 → Webcam")

choice = input("Enter choice: ")

if choice == "1":
    detector.detect_image("images/test.jpg")

elif choice == "2":
    detector.detect_video("videos/sample.mp4")

elif choice == "3":
    detector.detect_video(0)

else:
    print("Invalid option")
