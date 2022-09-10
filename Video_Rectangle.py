import cv2


def main():
	
	# reading the input
	cap = cv2.VideoCapture(0)

	output = cv2.VideoWriter(
		"output.avi", cv2.VideoWriter_fourcc(*'MPEG'),
	30, (1080, 1920))

	while(True):
		ret, frame = cap.read()
		if(ret):
			
			# adding filled rectangle on each frame
			cv2.rectangle(frame, (100, 150), (500, 600),
						(0, 255, 0), -1)
			
			# writing the new frame in output
			output.write(frame)
			cv2.imshow("output", frame)
			if cv2.waitKey(1) & 0xFF == ord('s'):
				break
		else:
			break

	cv2.destroyAllWindows()
	output.release()
	cap.release()


if _name_ == "_main_":
	main()
