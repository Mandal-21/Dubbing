import moviepy.editor as mpe

videoclip = mpe.VideoFileClip('thefile3.mp4')
audioclip = mpe.AudioFileClip('thefile3.mp4')
background_music = mpe.AudioFileClip("SilentAudio.mp3")
new_clip = videoclip.set_audio(background_music)
new_clip.write_videofile("final_cut1.mp4")
audioclip.write_audiofile('extracted_audiofile.mp3')
