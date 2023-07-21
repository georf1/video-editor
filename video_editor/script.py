import os
import random
import moviepy.editor as mp


def get_random_file(folder):
    files = os.listdir(folder)
    if not files:
        raise ValueError("The folder '{}' is empty.".format(folder))
    return os.path.join(folder, random.choice(files))


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Process "
                                     "video files and add music.")
    parser.add_argument("-f1", "--folder1",
                        type=str, required=True, help="Path to folder 1.")
    parser.add_argument("-f2", "--folder2",
                        type=str, required=True, help="Path to folder 2.")
    parser.add_argument("-m", "--music",
                        type=str, required=True, help="Path to music folder.")
    args = parser.parse_args()

    try:
        # Select first video
        video1_path = get_random_file(args.folder1)
        print("Selected video 1:", video1_path)

        # Select second video
        video2_path = get_random_file(args.folder2)
        print("Selected video 2:", video2_path)

        # Process video
        video1 = mp.VideoFileClip(video1_path).subclip(0, 2).set_fps(30)
        video2 = mp.VideoFileClip(video2_path).subclip(0, 2).set_fps(30)

        # Select and process music
        music_path = get_random_file(args.music)
        print("Selected music:", music_path)
        music = mp.AudioFileClip(music_path).subclip(0, 4)

        # Combine videos and add music
        final_video = mp.concatenate_videoclips([video1, video2],
                                                method='compose')
        final_video = final_video.set_audio(music)

        # Save the result
        output_path = "output.mp4"
        final_video.write_videofile(output_path)
        print("The final video has been saved to:", output_path)

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
