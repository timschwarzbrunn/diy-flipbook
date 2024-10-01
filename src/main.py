from argument_parser import get_args
import cv2
from datetime import datetime
from flipbook_generator import generate_flipbook
import imageio

# =========================================================================================
#       CONSTANTS
# =========================================================================================


CV2_WINDOW_NAME = "camera stream"


# =========================================================================================
#       MAIN VIDEO RECORDING LOOP / FLIPBOOK GENERATION
# =========================================================================================


def main():
    """
    This function opens a camera stream using OpenCV and write the video to a file.
    """
    # Parse the arguments / get the settings.
    args = get_args()

    # The main function handles two cases:
    # Case 1: A path to an existing file is passed to the program, then we will convert this video or GIF to
    #         a flipbook.
    # Case 2: No path is passed, then we will use the camera stream to capture a video, save if as a GIF and convert
    #         it to a flipbook.

    if args.filepath_video is not None:
        # Read in the video file and pass the frames to the flipbook generator.
        video_capture = cv2.VideoCapture(args.filepath_video)
        if video_capture.isOpened():
            # Extract all frames from the video.
            frames = []
            while True:
                # Read the next frame.
                ret, frame = video_capture.read()
                if not ret:
                    break
                frames.append(frame)
            # Generate the flipbook.
            filename_flipbook = (
                args.filepath_video[: args.filepath_video.rfind(".")] + "_flipbook.docx"
            )
            generate_flipbook(
                frames,
                args.height,
                args.left_margin,
                args.border_linewidth,
                args.sheet_margin,
                filename_flipbook,
            )
        else:
            print(f"Cannot open given file '{args.filepath_video}'.")
        video_capture.release()
    else:
        # Open the camera stream and the window.
        cv2.namedWindow(CV2_WINDOW_NAME)
        video_capture = cv2.VideoCapture(args.device_id)

        # When we create a GIF, we will first store all frames in a list and later save them to the disk.
        gif_frames = None

        if video_capture.isOpened():
            # Video recording loop.
            while True:
                # Capture the image.
                ret, frame = video_capture.read()
                if not ret:
                    break

                # Square?
                if args.square:
                    height, width, _ = frame.shape
                    if width > height:
                        frame = frame[
                            :,
                            int((width - height) / 2) : int((width - height) / 2)
                            + height,
                            :,
                        ]
                    elif height < width:
                        frame = frame[
                            int((height - width) / 2) : int((height - width) / 2)
                            + width,
                            :,
                            :,
                        ]
                    else:
                        # Already square.
                        pass

                # Display the camera stream.
                cv2.imshow(CV2_WINDOW_NAME, frame)

                # Save the image if we are currently recording.
                if gif_frames is not None:
                    gif_frames.append(frame)

                # Input handling.
                key = cv2.waitKey(int(1000.0 / args.fps))
                if key == 27 or key == ord("q"):
                    # Exit on ESC or q.
                    print("Exit program.")
                    break
                elif key == 32:
                    # Start / stop video recording on SPACE.
                    if gif_frames is None:
                        # Start recording.
                        print("\nStarted recording.")
                        gif_frames = []
                    else:
                        # Stop recording.
                        print("Stopped recording.")
                        timestamp = (
                            f"{datetime.now().year}{datetime.now().month:02d}{datetime.now().day:02d}"
                            + f"{datetime.now().hour:02d}{datetime.now().minute:02d}{datetime.now().second:02d}"
                        )
                        # Save the GIF.
                        print("Saving GIF ...")
                        filename_gif = timestamp + "_recording.gif"
                        # imageio uses RGB format, so convert.
                        imageio.mimsave(
                            filename_gif,
                            [
                                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                for frame in gif_frames
                            ],
                            fps=args.fps,
                        )
                        print(f"GIF saved to '{filename_gif}'.")
                        # Create a flipbook from the frames.
                        filename_flipbook = timestamp + "_flipbook.docx"
                        generate_flipbook(
                            gif_frames,
                            args.height,
                            args.left_margin,
                            args.sheet_margin,
                            filename_flipbook,
                        )
                        # Ready for the next one.
                        gif_frames = None
        else:
            print("Cannot open video stream.")
        # Terminate the windows and the camera stream.
        cv2.destroyWindow(CV2_WINDOW_NAME)
        video_capture.release()


# =========================================================================================
#       MAIN
# =========================================================================================

if __name__ == "__main__":
    main()
